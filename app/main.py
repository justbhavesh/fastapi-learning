from fastapi import FastAPI
from typing import Any
app = FastAPI()
@app.get("/")
def root():
    return{"greet":"Hello we are learning fastapi"}

@app.get("/shipment")
def new_shipment(id:int)->dict[str,int|str|float]:
    return {
        "id" : id,
        "content":"chair",
        "weight":12,
        "status":"placed"
        }

@app.get("/shipment/search")
def search_shipment(weight:float):
    return{
        "id":123,
        "content":"laptop",
        "weight":weight,
        "status":"in-transit"
    }
@app.post("/newship")
def body_type(data:dict)->str:
    return "oder placed successfully"

