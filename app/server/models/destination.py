from typing import Optional
from pydantic import BaseModel, Field


class DestinationSchema(BaseModel):
    coords: list = Field(...)
    url: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "coords": [51.05, -0.09],
                "url": "https://www.youtube.com/watch?v=saVFFwtZ1FU",
                "name": "sebastian",
                "description": "Puebla is a beautiful place!",
            }
        }


class UpdateDestinationModel(BaseModel):
    coords: Optional[list]
    url: Optional[str]
    name: Optional[str]
    description: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "coords": [51.10, -0.19],
                "url": "https://www.youtube.com/watch?v=saVFFwtZ1FU",
                "name": "sebastian",
                "description": "Puebla is a beautiful place!",
            }
        }


def ResponseModel(data, message):
    return {"data": [data], "code": 200, "message": message}


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
