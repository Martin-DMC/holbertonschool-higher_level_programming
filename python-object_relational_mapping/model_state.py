#!/usr/bin/python3
"""
this module make a python file that contains the class
definition of a State and an instance Base = declarative_base()
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    this class create a table links to the MySQL table 'states'.
    inheriting of the base class that i import of sqlalchemy
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")
