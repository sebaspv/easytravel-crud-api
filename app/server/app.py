from fastapi import FastAPI
from .routes.destination import router as DestinationRouter

app = FastAPI()
app.include_router(DestinationRouter, tags=["Destination"], prefix="/destination")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message":"prueba xd"}