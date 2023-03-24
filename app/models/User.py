import datetime

from sqlmodel import Field, SQLModel, Relationship

import sqlalchemy as sa

from typing import Optional


class User(SQLModel, table=True):
    __tablename__ = "users"

    user_id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str = Field(sa_column=sa.Column(sa.TEXT, nullable=False, unique=True))
    last_name: str = Field(sa_column=sa.Column(sa.TEXT, nullable=False, unique=True))
    username: str = Field(sa_column=sa.Column(sa.TEXT, nullable=False, unique=True))
    email: str = Field(sa_column=sa.Column(sa.TEXT, nullable=False, unique=True))
    birthdate: datetime.date = Field(sa_column=sa.Column(sa.DATE, nullable=False, unique=True))
    created_at: datetime.datetime = Field(sa_column=sa.Column(sa.DateTime(timezone=True), default=sa.func.now()))

    passwords: list["UserPassword"] = Relationship(back_populates="user")
