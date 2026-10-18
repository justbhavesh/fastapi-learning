# pydantic

from pydantic import BaseModel, EmailStr
from enum import Enum


class ShipmentStatus(str,Enum):
    SHIPPED = "shippied"
    DELIVERED ="delivered"
    PLACED ="placed"
    INTRANSIT ="in_transit"

class Ship(BaseModel):
   
    content: str
    weight: float


class ResponseModal(BaseModel):
    id : int
    content: str
    weight: float
    status: str

class updateShipment(Ship):
    pass

class CreateUser(BaseModel):
    id:int
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id:int
    username: str
    email: EmailStr




# additional


class SignIn(BaseModel):
    email: EmailStr
    password: str


class SignInResponse(BaseModel):
    message:str
    userid:str
    username:str
    email:EmailStr


#**************** LOGOUT **********#

class Logout(BaseModel):
    email: EmailStr
    password: str  
    token: str  