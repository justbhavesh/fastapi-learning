import os
from dotenv import load_dotenv
from datetime import date, datetime,timezone, timedelta
from fastapi import HTTPException
from jose import JWTError, jwt
from sqlmodel import Session
 
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
if not SECRET_KEY:
    raise RuntimeError("secret keys not configured")

if not ALGORITHM:
    raise RuntimeError("algorithm not configured")

def generate_token(user_id: int):
    payload = {
        "sub": str(user_id),
        "exp": datetime.now(timezone.utc) + timedelta(minutes=30),
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

print(generate_token(15))  # Example usage, replace with actual user ID

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status=401)
        return user_id
    except JWTError:
        raise HTTPException(status=401, detail="Token has expired")


# check if a token has been logged out/revoked 

def is_token_revoked(token:str,session: Session) -> 
    




