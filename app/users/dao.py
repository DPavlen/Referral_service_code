from users.schemas import SReferralCode
from database import async_session_maker
from dao.base import BaseDAO
from users.models import User, ReferralCode
from sqlalchemy import select, insert, update, text
from sqlalchemy.orm import selectinload, load_only



class UserDao(BaseDAO):
    """Класс для CRUD-операций связанных с пользователями."""
    model = User

    @classmethod
    async def get_user_and_codes(cls, **filter_by):
        async with async_session_maker() as session:

            query = (
                select(cls.model)
                .filter_by(**filter_by)
                .options(selectinload(cls.model.referral_codes), 
                         load_only(cls.model.id, cls.model.email))
            )
            result = await session.execute(query)
            return result.scalar_one_or_none()
            # return result.mappings().one_or_none()
    

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()


class ReferralCodeDAO(BaseDAO):
    """Класс для CRUD-операций связанных с реферальными кодами."""
    model = ReferralCode

    @classmethod
    async def add_ref_code(cls, data: SReferralCode):
        new_ref_code = insert(cls.model).values(

            code=data.code,
            expiration_date=data.expiration_date,
            user_id=data.user_id
        )
        query = select(cls.model.code)

        async with async_session_maker() as session:
            res = await session.execute(query)
            existing_codes = res.scalars().all() 
            if data.code in existing_codes:
                return {"message": "Code already exists"}
            else:
                await session.execute(new_ref_code)
                await session.commit()
                return {"message": "Code has been successfully created"}