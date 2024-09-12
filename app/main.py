from fastapi import FastAPI
from app.routers import tasks, websocket
from app.database import database, engine, metadata

metadata.create_all(engine)

app = FastAPI()

# Register routers
app.include_router(tasks.router)
app.include_router(websocket.router)


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()