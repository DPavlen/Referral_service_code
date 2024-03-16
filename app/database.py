from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, sessionmaker
# for revision
# from .config import settings

# for uvicorn --reload
# from app.config import settings
from config import settings


DATABASE_URL = settings.DATABASE_URL
DATABASE_PARAMS = {"poolclass": NullPool}

# engine = create_async_engine(DATABASE_URL)
engine = create_async_engine(DATABASE_URL, **DATABASE_PARAMS)
engine_nullpool = create_async_engine(DATABASE_URL, poolclass=NullPool)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
async_session_maker_nullpool = async_sessionmaker(engine_nullpool, expire_on_commit=False)

class Base(DeclarativeBase):
    """Собирает все данные о моделях.
    Аккамулириует для миграцй Alembica."""
    pass