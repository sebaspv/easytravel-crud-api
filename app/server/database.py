import motor.motor_asyncio
from bson.objectid import ObjectId
from decouple import config

MONGO_DETAILS = config('MONGO_DETAILS')
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.destinations
destination_collection = database.get_collection("destinations_collection")


def destination_helper(destination) -> dict:
    return {
        "id": str(destination["_id"]),
        "coords": destination["coords"],
        "url": destination["url"],
        "name": destination["name"],
        "description": destination["description"],
    }


async def retrieve_destinations():
    destinations = []
    async for destination in destination_collection.find():
        destinations.append(destination_helper(destination))
    return destinations


async def add_destination(destination_data: dict) -> dict:
    destination = await destination_collection.insert_one(destination_data)
    new_destination = await destination_collection.find_one({"_id": destination.inserted_id})
    return destination_helper(new_destination)


async def retrieve_destination(id: str) -> dict:
    destination = await destination_collection.find_one({"_id": ObjectId(id)})
    if destination:
        return destination_helper(destination)


async def update_destination(id: str, data: str):
    if len(data) < 1:
        return False
    destination = await destination_collection.find_one({"_id": ObjectId(id)})
    if destination:
        updated_destination = await destination_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_destination:
            return True
        return False


async def delete_destination(id: str):
    destination = await destination_collection.find_one({"_id": ObjectId(id)})
    if destination:
        await destination_collection.delete_one({"_id": ObjectId(id)})
        return True
