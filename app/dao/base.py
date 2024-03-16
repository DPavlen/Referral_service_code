from sqlalchemy import delete, insert, select
from sqlalchemy.exc import SQLAlchemyError

from database import async_session_maker


class BaseDAO:
    """Объект доступа к данным."""
    model = None

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        """Поиск записи по фильтру."""
        async with async_session_maker() as session:
            # query = select(cls.model.__table__.columns).filter_by(**filter_by)
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            # return result.mappings().one_or_none()
            return result.scalars().all()

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            # query = select(cls.model.__tablename__.columns).filter_by(**filter_by)
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            # return result.mappings().all()
            return result.scalar_one_or_none()
    
    # @classmethod
    # async def delete(cls, **filter_by):
    #     async with async_session_maker() as session:
    #         query = delete(cls.model).filter_by(**filter_by)
    #         await session.execute(query)
    #         await session.commit()

    # @classmethod
    # async def add(cls, **data):
    #     """
    #     Добавляет новую запись в таблицу, используя переданные данные.
    #     Parameters:
    #     cls (class): Класс DAO.
    #     **data: Ключевые аргументы с данными для добавления в таблицу.
    #     Returns:
    #     dict: Словарь с данными новой записи, включая идентификатор (id).
    #     Если произошла ошибка при вставке данных, возвращается None.
    #     """
    #     try:
    #         query = insert(cls.model).values(**data).returning(cls.model.id)
    #         async with async_session_maker() as session:
    #             result = await session.execute(query)
    #             await session.commit()
    #             return result.mappings().first()
    #     except (SQLAlchemyError, Exception) as e:
    #         if isinstance(e, SQLAlchemyError):
    #             msg = "Database Exc: Cannot insert data into table"
    #         elif isinstance(e, Exception):
    #             msg = "Unknown Exc: Cannot insert data into table"

    #         return None
    
    # @classmethod
    # async def add(cls, **data):
    #     async with async_session_maker() as session:
    #         query = insert(cls.model).values(**data)
    #         await session.execute(query)
    #         await session.commit()
