from fastapi import FastAPI
from routers import players, events
from contextlib import asynccontextmanager
from database.database import create_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up!")
    create_db()
    yield
    print("Shutting down....")

app = FastAPI(lifespan=lifespan)

app.include_router(players.router)
app.include_router(events.router)