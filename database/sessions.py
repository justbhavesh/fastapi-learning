import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlmodel import SQLModel
from database.models import Shipment,ShipmentStatus

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


engine=create_engine(
    url=DATABASE_URL, echo=True
    )
def create_db_and_table():
    SQLModel.metadata.create_all(bind=engine)


def get_session():
    with Session(engine) as db:
        yield db
