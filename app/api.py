from fastapi import FastAPI, HTTPException

from app.auth import generate_token
from app.hash import generate_password
from app.schema import CreateUser, Ship, ShipmentStatus, SignInResponse, UserResponse

from app.db import Database
from database.sessions import get_session


#*******************additional imports***********#

from fastapi import Depends, status
from sqlmodel import Session, or_, select
from app.schema import SignIn, SignInResponse
from app.hash import check_password





app=FastAPI()
db=Database("supply.db")

# @app.get("/shipments/{sid}")
# def get_shipments(sid:int):
#     shipment = db.get_shipment(sid)
#     return shipment
@app.put("/update-shipment/{sid}")
def create_shipment(data:Ship):
    new_id= db.create_shipment(data)
    return {"new_id":new_id}


from contextlib import contextmanager
from sqlmodel import SQLModel
from database.models import Shipment,ShipmentStatus, User

@contextmanager
async def lifespan(app:FastAPI):
    create_db_and_table()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("create-user",response_model=UserResponse)
def create_new_user(data:UserCreate,session:Session=Depends(get_session)):
    existing_user = session.exec(select(User).where(or_(User.username == data.username, User.email == data.email)).first())
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="user name or email already taken")
    hashed_password = generate_password(data.password)
    user = User(username=data.username, email=data.email, password=hashed_password)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@app.post("/new-shipment")  
def new_shipment(data:Ship, session:Session=Depends(get_session)):
    Shipment=Shipment.model_validate=(data.model_dump())
    session.add(Shipment)
    session.commit()
    session.refresh(Shipment)
    return Shipment
    
@app.get("/shipments")
def get_shipments():
    pass


# additional


@app.post("/signin", response_model=SignInResponse)
def signin(
    data: SignIn,
    session: Session = Depends(get_session)
):
    user = session.exec(
        select(User).where(User.email == data.email)
    ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid username or password"
        )
    password = check_password(data.password, user.password)

    if not check_password(data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    token = generate_token(user.id)

    return SignInResponse(
        message="Login successful",
        userid=str(user.id),
        username=user.username,
        email=user.email,
        token=token
    )