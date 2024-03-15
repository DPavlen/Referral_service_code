from datetime import date
from sqlalchemy import Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship, mapped_column, Mapped

from database import Base


class User(Base):
    """
    Модель пользователя.
    Описание в соответствии с SQLAlchemy версии 2.
    Attributes:
        __tablename__ (str): Имя таблицы в БД.
        id (int): Первичный ключ пользователя.
        email (str): Электронная почта пользователя.
        hashed_password (str): Захешированный пароль пользователя.
        referral_codes (list[ReferralCode]): Список реферальных кодов пользователя.
    Methods:
        __str__: Возвращает строковое представление пользователя.
    """
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
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

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(nullable=False)
    expiration_date: Mapped[date] = mapped_column(Date)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="referral_codes")
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)

    def __str__(self):
        return f"Код пользователя {self.code}"