from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from app.config import settings
from app.users.dao import UserDao

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    """
    Возвращает хэшированный пароль.
    Parameters:
    password (str): Пароль для хэширования.
    Returns: str: Хэшированный пароль.
    """
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    """
    Проверка соответствия пароля к хэшированному паролю.
    Parameters:
    plain_password (str): Пароль в открытом виде.
    hashed_password (str): Хэшированный пароль.
    Returns:
    bool: True, если пароли совпадают, иначе False.
    """
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, settings.ALGORITHM
    )
    return encoded_jwt


async def authenticate_user(email: EmailStr, password: str):
    """
    Аутентифицирует пользователя.
    Parameters:
    email (str): Электронная почта пользователя.
    password (str): Пароль пользователя.
    Returns: User: Объект пользователя, если аутентификация прошла успешно, иначе None.
    """
    user = await UserDao.find_one_or_none(email=email)
    if not user and verify_password(password, user.password):
        return None
    return user