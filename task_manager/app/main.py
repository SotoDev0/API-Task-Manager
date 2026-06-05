from fastapi import FastAPI
from .routers import auth
from .database import engine, Base
from .routers import tasks
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="Task Manager API", lifespan=lifespan)
app.include_router(auth.router)
app.include_router(tasks.router)