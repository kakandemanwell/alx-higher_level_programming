#!/usr/bin/python3
"""Class definition of a City and an instance Base of declarative_base()"""


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """class that inherits from Base"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
