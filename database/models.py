from datetime import datetime
from enum import Enum

from sqlmodel import Field, SQLModel

class ShipmentStatus(str,Enum):
    placed="placed"
    delivered="delivered"
    in_tansit="in_transit"
    cancelled="cancelled"
    pending="pending"
    shipped="shipped"

class Shipment(SQLModel,table=True):
    __tablename__="shipments"
    id:int|None = Field(default=None,primary_key=True)
    content:str
    weight:float =Field(ge=0,le=20)
    status:ShipmentStatus= Field(default=ShipmentStatus.placed)
    destination:str
    expected_delivery:datetime
    status:ShipmentStatus=Field(ShipmentStatus.placed)

class User(SQLModel,table=True):
    __tablename__="users"
    id:int|None = Field(default=None,primary_key=True)
    username:str = Field(unique=True)
    email:str =  Field(unique=True)
    password:str


#*************** LOGOUT **************#

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    email: str = Field(unique=True)
    password: str