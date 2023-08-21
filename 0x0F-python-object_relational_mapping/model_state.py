#!/usr/bin/python3
""" class definition of a State and an instance Base = declarative_base() """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """ Represents a state for a MySQL db
    __tablename__(str): name of table to store states
    id (sqlalchemy.Integer): state id
    name (sqlalchemy.String(: state name
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name =  Column(String(128), nullable=False)
