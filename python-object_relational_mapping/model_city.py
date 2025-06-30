#!/usr/bin/python3
"""
this module make a python file that contains the class
definition of a City
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """
    this class create a table links to the MySQL table 'cities'.
    inheriting of the base class that i import of sqlalchemy
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
