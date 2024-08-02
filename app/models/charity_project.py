from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
import datetime
from core.db import PreBase


class CharityProject(PreBase):

    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, default=0)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.datetime.utcnow())
    close_date = Column(DateTime, nullable=True)