from pydantic import BaseModel, EmailStr


class SUserRegister(BaseModel):
    """Схема регистрации пользователя.
    Валидация email и password.
    """
    email: EmailStr
    password: str