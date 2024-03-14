from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.config import settings

DATABASE_URL = settings.DATABASE_URL

from app.config import settings

# if settings.MODE == "TEST":
#     DATABASE_URL = settings.TEST_DATABASE_URL
#     DATABASE_PARAMS = {"poolclass": NullPool}
# else:
#     DATABASE_URL = settings.DATABASE_URL
#     DATABASE_PARAMS = {}

# engine = create_async_engine(DATABASE_URL, **DATABASE_PARAMS)
# engine_nullpool = create_async_engine(DATABASE_URL, poolclass=NullPool)
#
# # Во 2.0 версии Алхимии был добавлен async_sessionamaker.
# async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
# async_session_maker_nullpool = async_sessionmaker(engine_nullpool, expire_on_commit=False)

engine = create_async_engine(DATABASE_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    """Собирает все данные о моделях.
    Аккамулириует для миграцй Alembica."""
    pass