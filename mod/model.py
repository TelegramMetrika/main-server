import sqlalchemy as sa
from .db import SqlAlchemyBase

class Metrika(SqlAlchemyBase):
    __tablename__ = 'bots'
    __table_args__ = {'extend_existing': True}

    id = sa.Column(sa.Integer,
                   primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=True)
    token = sa.Column(sa.String, nullable=True)
    users = sa.Column(sa.String, nullable=True)

from typing import Optional
from pydantic import BaseModel

class Body(BaseModel):
    user: str