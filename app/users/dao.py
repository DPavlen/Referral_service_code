from database import async_session_maker
from dao.base import BaseDAO
from users.models import User, ReferralCode
from sqlalchemy import select, insert, update, text
from sqlalchemy.orm import selectinload, load_only



class UserDao(BaseDAO):
    """Класс для CRUD-операций связанных с пользователями."""
    users = User