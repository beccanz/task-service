from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL = "sqlite+aiosqlite:///./local.db"

# for postgres connection
# postgres+asyncpg://user:password@localhost:5432/dbname

engine = create_async_engine(
    DATABASE_URL,
    echo=True, #logs sql (turn off in prod)
)