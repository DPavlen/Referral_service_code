from app.dao.base import BaseDAO
from app.users.models import User


class UserDao(BaseDAO):
    """Класс для CRUD-операций связанных с пользователями."""
    users = User
