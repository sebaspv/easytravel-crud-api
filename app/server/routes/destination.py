from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from uuid import uuid4

from server.database import (
    add_destination,
    delete_destination,
    retrieve_destination,
    retrieve_destinations,
    update_destination,
)
from server.models.destination import (
    ErrorResponseModel,
    ResponseModel,
    DestinationSchema,
    UpdateDestinationModel,
)

router = APIRouter()

@router.post("/", response_description="Added destination to database")
async def add_destination_data(destination: DestinationSchema = Body(...)):
    destination = jsonable_encoder(destination)
    new_destination = await add_destination(destination)
    return ResponseModel(new_destination, "Destination added successfully.")

@router.get("/", response_description="Destinations retrieved")
async def get_destinations():
    destinations = await retrieve_destinations()
    if destinations:
        return ResponseModel(destinations, "Destinations retrieved succesfully")
    return ResponseModel(destinations, "There are no destinations stored")

@router.get("/{id}", response_description="Destination retrieved")
async def get_destination(id):
    destination = await retrieve_destination(id)
    if destination:
        return ResponseModel(destination, "Destination retrieved succesfully")
    return ErrorResponseModel("Fix your code lmao", 404, "This destination doesn't exist")

@router.delete("/{id}", response_description="Destination data deleted from the database")
async def delete_destination_data(id: str):
    deleted_destination = await delete_destination(id)
    if deleted_destination:
        return ResponseModel(
            "Destination with ID: {} removed".format(id), "Destination deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Destination with id {0} doesn't exist".format(id)
    )