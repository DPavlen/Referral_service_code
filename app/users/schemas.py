import re
from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, validator, Field


class SUserAuth(BaseModel):
    """Схема регистрации пользователя, входа по логину.
    Валидация email и password.
    """
    # orm_mode в 2 версии Pydantic
    model_config = ConfigDict(from_attributes=True)

    name: str
    family_name: str
    middle_name: str
    email: EmailStr
    password: str

    @validator("email")
    @classmethod
    def validate_email(cls, value):
        if not bool(re.fullmatch(r'[\w.-]+@[\w-]+\.[\w.]+', value)):
            raise ValueError("Email is invalid")
        return value


class SReferralCode(BaseModel):
    """Схема получения реферальных кодов.
    model_config - Extra JSON Schema data in Pydantic models V.2
    """

    id: Optional[int] = None
    code: str = Field(..., min_length=1)
    expiration_date: Optional[date] = None
    user_id: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"id": 1,
                 "code": "write something",
                 "user_id": 1,
                 "expiration_date": "2024-03-16"
                 }
            ],
        }
    }
