from http.client import HTTPException

from fastapi import APIRouter, Depends, Response

from app.users.auth import get_password_hash
from app.users.dao import UserDao
from app.users.models import User
from app.users.schemas import SUserRegister

router_auth = APIRouter(
    prefix="/auth",
    tags=["Аутентификация"],
)

router_users = APIRouter(
    prefix="/users",
    tags=["Пользователи"],
)


@router_auth.post("/register", status_code=201)
async def register_user(user_data: SUserRegister):
    """
    Регистрация нового пользователя.
    Parameters:
    user_data (SUserRegister): Данные пользователя, переданные в запросе.
    Returns: dict: Словарь с данными нового пользователя.
    Raises: HTTPException: Если пользователь с указанным адресом электронной почты уже существует.
    """
    existing_user = await UserDao.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=500)
    hashed_password = get_password_hash(user_data.password)
    await UserDao.add(email=user_data.email, hashed_password=hashed_password)
