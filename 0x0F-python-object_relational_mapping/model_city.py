#!/usr/bin/python3
"""Cities in State"""
from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base

# Create class to represent table cities
class City(Base):
    """This class represents the table cities in the database"""
    __tablename__ = "cities"

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
