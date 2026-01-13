from fastapi import FastAPI
from app.api.routes import router as health_router

from app.db.database import engine
from app.db.base import Base
from app.db import models


app = FastAPI()

app.include_router(health_router)

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
