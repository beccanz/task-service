import os
from sqlalchemy.ext.asyncio import create_async_engine

# Use PostgreSQL by default, fallback to SQLite for local testing without Docker
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://taskuser:taskpass@localhost:5432/taskdb"
)

engine = create_async_engine(
    DATABASE_URL,
    echo=True,  # logs SQL (turn off in prod)
    pool_pre_ping=True,  # verify connections before using
)