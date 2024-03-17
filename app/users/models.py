from datetime import date

from sqlalchemy import Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship, mapped_column, Mapped

# for uvicorn --reload
from app.database import Base


# for revision
# from ..database import Base


class User(Base):
    """
    Модель пользователя.
    Описание в соответствии с SQLAlchemy версии 2.
    Attributes:
        __tablename__ (str): Имя таблицы в БД.
        id (int): Первичный ключ пользователя.
        name (str): Имя пользователя.
        family_name (str): Фамилия пользователя.
        middle_name (str): Отчество пользователя.
        email (str): Электронная почта пользователя.
        hashed_password (str): Захешированный пароль пользователя.
        referral_codes (list[ReferralCode]): Список реферальных кодов пользователя.
    Methods:
        __str__: Возвращает строковое представление пользователя.
    """
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, comment="PK таблицы users")
    name: Mapped[str] = mapped_column(nullable=True, comment="Имя пользователя")
    family_name: Mapped[str] = mapped_column(nullable=True, comment="Фамилия пользователя")
    middle_name: Mapped[str] = mapped_column(nullable=True, comment="Отчество пользователя")
    email: Mapped[str] = mapped_column(nullable=False, comment="Электронная почта пользователя")
    hashed_password: Mapped[str] = mapped_column(nullable=False, comment="Хэш-пароль пользователя")
    referral_codes: Mapped[list["ReferralCode"]] = relationship(
        "ReferralCode", back_populates="user")

    def __str__(self):
        return f"Пользователь {self.email}"


class ReferralCode(Base):
    """
    Модель реферального кода.
    Attributes:
        __tablename__ (str): Имя таблицы в БД.
        id (int): Первичный ключ реферального кода.
        code (str): Реферальный код.
        expiration_date (date): Дата истечения срока действия реферального кода.
        user_id (int): Внешний ключ на пользователя, к которому привязан реферальный код.
        user (User): Объект пользователя, связанный с данным реферальным кодом.
        is_active (bool): Флаг, указывающий на активность реферального кода.
    Methods:
        __str__: Возвращает строковое представление реферального кода.
    """
    __tablename__ = "referral_codes"

    id: Mapped[int] = mapped_column(primary_key=True, comment="PK таблицы referral_codes")
    code: Mapped[str] = mapped_column(nullable=False, comment="Реферальный код")
    expiration_date: Mapped[date] = mapped_column(Date, comment="Дата истечения срока действия кода")
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), comment="FK на user")
    user: Mapped["User"] = relationship(back_populates="referral_codes", doc="Связь с пользователем")
    is_active: Mapped[bool] = mapped_column(Boolean, default=False, comment="Флаг активности кода")

    def __str__(self):
        return f"Пользователь {self.user_id} и его код {self.code}"
