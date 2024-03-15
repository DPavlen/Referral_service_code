from pydantic import BaseModel, EmailStr


class SUserAuth(BaseModel):
    """Схема регистрации пользователя.
    Валидация email и password.
    """
    email: EmailStr
    password: str