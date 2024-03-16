"""Update User & ReferralCode

Revision ID: 503c709e4e77
Revises: 435ceb777b6f
Create Date: 2024-03-16 17:36:38.363054

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '503c709e4e77'
down_revision: Union[str, None] = '435ceb777b6f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('referral_codes', 'id',
               existing_type=sa.INTEGER(),
               comment='PK таблицы referral_codes',
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('referral_codes', 'code',
               existing_type=sa.VARCHAR(),
               comment='Реферальный код',
               existing_nullable=False)
    op.alter_column('referral_codes', 'expiration_date',
               existing_type=sa.DATE(),
               comment='Дата истечения срока действия кода',
               existing_nullable=False)
    op.alter_column('referral_codes', 'user_id',
               existing_type=sa.INTEGER(),
               comment='FK на user',
               existing_nullable=False)
    op.alter_column('referral_codes', 'is_active',
               existing_type=sa.BOOLEAN(),
               comment='Флаг активности кода',
               existing_nullable=False)
    op.add_column('users', sa.Column('name', sa.String(), nullable=False, comment='Имя пользователя'))
    op.add_column('users', sa.Column('family_name', sa.String(), nullable=False, comment='Фамилия пользователя'))
    op.add_column('users', sa.Column('middle_name', sa.String(), nullable=False, comment='Отчество пользователя'))
    op.alter_column('users', 'id',
               existing_type=sa.INTEGER(),
               comment='PK таблицы users',
               existing_nullable=False,
               autoincrement=True,
               existing_server_default=sa.text("nextval('users_id_seq'::regclass)"))
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(),
               comment='Электронная почта пользователя',
               existing_nullable=False)
    op.alter_column('users', 'hashed_password',
               existing_type=sa.VARCHAR(),
               comment='Хэш-пароль пользователя',
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'hashed_password',
               existing_type=sa.VARCHAR(),
               comment=None,
               existing_comment='Хэш-пароль пользователя',
               existing_nullable=False)
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(),
               comment=None,
               existing_comment='Электронная почта пользователя',
               existing_nullable=False)
    op.alter_column('users', 'id',
               existing_type=sa.INTEGER(),
               comment=None,
               existing_comment='PK таблицы users',
               existing_nullable=False,
               autoincrement=True,
               existing_server_default=sa.text("nextval('users_id_seq'::regclass)"))
    op.drop_column('users', 'middle_name')
    op.drop_column('users', 'family_name')
    op.drop_column('users', 'name')
    op.alter_column('referral_codes', 'is_active',
               existing_type=sa.BOOLEAN(),
               comment=None,
               existing_comment='Флаг активности кода',
               existing_nullable=False)
    op.alter_column('referral_codes', 'user_id',
               existing_type=sa.INTEGER(),
               comment=None,
               existing_comment='FK на user',
               existing_nullable=False)
    op.alter_column('referral_codes', 'expiration_date',
               existing_type=sa.DATE(),
               comment=None,
               existing_comment='Дата истечения срока действия кода',
               existing_nullable=False)
    op.alter_column('referral_codes', 'code',
               existing_type=sa.VARCHAR(),
               comment=None,
               existing_comment='Реферальный код',
               existing_nullable=False)
    op.alter_column('referral_codes', 'id',
               existing_type=sa.INTEGER(),
               comment=None,
               existing_comment='PK таблицы referral_codes',
               existing_nullable=False,
               autoincrement=True)
    # ### end Alembic commands ###
