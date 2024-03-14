from datetime import date
from sqlalchemy import Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship, mapped_column, Mapped

from app.database import Base


class User(Base):
    """Модель юзера. Описание в соответсвии с Алхимии vers.2."""
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    referral_codes: Mapped[list["ReferralCode"]] = relationship(
        "ReferralCode", back_populates="user")

    def __str__(self):
        return f"Пользователь {self.email}"


class ReferralCode(Base):
    """Модель реферального кода."""
    __tablename__ = "referral_codes"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(nullable=False)
    expiration_date: Mapped[date] = mapped_column(Date)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="referral_codes")
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)

    def __str__(self):
        return f"Код пользователя {self.code}"