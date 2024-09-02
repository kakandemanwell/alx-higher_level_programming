#!/usr/bin/python3

"""
This module contains the class definition of State
and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

class City(Base):
    """

    City class that inherits from Base

    Attributes:

        tablename (str): The table name of the class

        id (int): The City id of the class

        name (str): The City name of the class

        state_id (int): The State id of the city

    """

    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
