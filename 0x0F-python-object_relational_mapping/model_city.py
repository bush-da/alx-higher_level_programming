#!/usr/bin/python3
""" contains the class definition of a City """

from model_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

class City(Base):
    """ Represent a state for a MySQL db
    __tablename__(str): name of table to store cities
    id (sqlalchemy.Integer): city id
    name (sqlalchemy.String): city name
    state_id (sqlclchemy.Interger): forign key to state.id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = (Integer, ForeignKey("states.id"), nullable=False)
