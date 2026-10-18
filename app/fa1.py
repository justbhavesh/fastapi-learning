
from fastapi import FastAPI,HTTPException,status,Body
from app.schema import Ship,  ShipmentStatus, updateShipment

app=FastAPI()

shipments = {
    1270:
      {"weight": 12.5, "content": "wooden table", "status": "delivered"},
    1271:
      {"weight": 13.5, "content": "toys", "status": "pending"},
    1272:
      {"weight": 10.2, "content": "chair", "status": "shipped"},
    1273:
      {"weight": 5.1, "content": "books", "status": "pending"},
    1274:
      {"weight": 22.0, "content": "refrigerator", "status": "delivered"},
    1275:
      {"weight": 3.7, "content": "clothes", "status": "shipped"},
    1276:
      {"weight": 8.9, "content": "shoes", "status": "pending"},
    1277:
      {"weight": 15.0, "content": "monitor", "status": "delivered"},
    1278:
      {"weight": 6.3, "content": "keyboard", "status": "shipped"},
    1279:
      {"weight": 1.1, "content": "mouse", "status": "pending"},
}

@app.get("/shipment/{shipment_id}")
def get_shipments_by_id(shipment_id:int):
    ship_id= shipment_id
    shipment=shipments.get(ship_id)
    if shipment is None:
        raise  HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Prodect with that id is not found"
        )

    return shipment

@app.get("shipment/latest")
def latest_shipment():
    latest_id=max(shipments.key())
    return {"latest shipment":latest_id}


# post request
    @app.post("/new-shipment")
    def new_shipment(weight:float=Body(...),content:str=Body(...)):
        if weight<=0:
            raise  HTTPException(
                        status_code=status.HTTP_406_NOT_ACCEPTABLE,
                        detail="weight must be greater than 0",

                    )
        new_id = max(shipments)+1

        new_shipments={
            "id":new_id,
            "weight":weight,
            "content":content,
            "status":"placed",
        }

        shipments[new_id] = new_shipments

        return {"message":"order placed successfully{new_id}"}
    


# data edit (put)

@app.put("/update-shipment/{ship_id}")
def update_shipment(ship_id:int,weight:float,content:str):
    if ship_id not in shipments:
        raise HTTPException (
            status_code=status.HTTP_404_NOT_FOUND,
            details="Product with this id is not available"
        )

    shipments[ship_id].update({"weight":weight,"content":content})
    return {"message":"shipment is updated","data":shipments[ship_id]}
    


# update specific part only

@app.patch("/update-shipment/{ship_id}")
def update_only_one(ship_id:int,weight:float | None=Body(None) ,content:str | None=Body(None)):
    if ship_id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            details="Product with this id is not available"

        )    
    shipments[ship_id].update({"weight":weight,"content":content})
    return {"message":"shipment is updated","data":shipments[ship_id]}




@app.delete("/remove-shipment{ship_id}")
def remove_shipment(ship_id:int):
    if ship_id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="order eith this id doesnot exist",

            )
    shipments.pop(ship_id)
    return{"message": f"shipment with the #{ship_id} delete successfully"}







@app.post("/new-shipment")
def new_shipment(weight:float=Body(...),content:str=Body(...)):
        if weight<=0:
            raise  HTTPException(
                        status_code=status.HTTP_406_NOT_ACCEPTABLE,
                        detail="weight must be greater than 0",

                    )
        new_id = max(shipments)+1

        new_shipments={
            "id":new_id,
            "weight":weight,
            "content":content,
            "status":"placed",
        }

        shipments[new_id] = new_shipments

        return {"message":"order placed successfully{new_id}"}
    

# post request using pydantic

# @app.post("/create-shipment",ResponseModel=Response)
# def create_shipment(shipmentss:Ship):
#     if shipmentss.weight:
#         new_id = shipmentss.id
#         new_content ={
#             "id": new_id,
#             "weight": shipmentss.weight,
#             "content":shipmentss.content,
#             "status":"placed",
#         }
#         shipments.update({new_id: new_content})
#     return shipments[new_id]
    
        



@app.put("/update-shipment/{sid}")
def update_shipment(data: updateShipment,sid):
    if sid not in shipments:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="product with this id not found",)
    shipments[sid]={
        "id":sid,
        "content":data.content
        **data.model_dump(),
        "status":ShipmentStatus.PLACED,
        
    }
    return shipments[sid]


