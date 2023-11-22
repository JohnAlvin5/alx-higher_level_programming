#!/usr/bin/python3
""" defines a state model."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ represents a class state"""
    __tablename__ = "states"
    id = Column(Integer,unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
