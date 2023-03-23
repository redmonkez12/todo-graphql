import datetime

from sqlmodel import SQLModel, Field
from typing import Optional

import sqlalchemy as sa


class Todo(SQLModel, table=True):
    __tablename__ = "todos"

    id: Optional[int] = Field(default=None, primary_key=True)
    label: str = Field(sa_column=sa.Column(sa.TEXT, nullable=False, unique=True))
    created_at: datetime.datetime = Field(sa_column=sa.Column(sa.DateTime(timezone=True), default=sa.func.now()))
