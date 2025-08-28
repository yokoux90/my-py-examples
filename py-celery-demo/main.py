from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
import uvicorn
from db import create_db_and_tables
import handler


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Startup App")
    # SetUp
    create_db_and_tables()
    # Running
    yield
    # TearDown
    logger.info("Shutdown App")


app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(handler.router)

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
