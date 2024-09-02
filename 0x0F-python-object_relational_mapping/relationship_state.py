#!/usr/bin/python3

"""
This module contains the class definition of State
and an instance Base = declarative_base()
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
#from relationship_city import City

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
