from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine
)

from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite+aiosqlite:///./local.db"

# for postgres connection
# postgres+asyncpg://user:password@localhost:5432/dbname

engine = create_async_engine(
    DATABASE_URL,
    echo=True, #logs sql (turn off in prod)
)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

Base = declarative_base
