from http.client import HTTPException

from fastapi import APIRouter, Response, Depends, HTTPException

from app.users.auth import (
    get_password_hash,
    authenticate_user,
    create_access_token
)
from app.users.dao import UserDao
from app.users.dependencies import get_current_user
from app.users.models import User
from app.users.schemas import SUserAuth

router = APIRouter(
    prefix="/auth",
    tags=["Авторизация и рагистрация пользователей"],
)


@router.post("/register")
async def register_user(user_data: SUserAuth):
    """
    Регистрация нового пользователя.
    Parameters:
    user_data (SUserRegister): Данные пользователя, переданные в запросе.
    Returns: dict: Словарь с данными нового пользователя.
    Raises: HTTPException: Если пользователь с указанным адресом электронной почты уже существует.
    """
    existing_user = await UserDao.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=500, detail="User is already existing")
    hashed_password = get_password_hash(user_data.password)
    await UserDao.add(email=user_data.email, hashed_password=hashed_password)
    return {"message": "Регистрация прошла успешно!"}


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    """Вход по логину."""
    user = await authenticate_user(user_data.email, user_data.password)
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("referral_access_token", access_token, httponly=True)
    # TODO refresh token
    return {"referral_access_token": access_token}


@router.post("/logout")
async def logout_user(response: Response):
    """Выход пользователя и удаление токена."""
    return response.delete_cookie("access_token")


@router.get("/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    """Возвращает текущего пользователя."""
    return current_user
