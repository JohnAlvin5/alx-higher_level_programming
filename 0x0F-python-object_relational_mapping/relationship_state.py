#!/usr/bin/python3
""" defines a model state"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

mymeta= MetaData()
Base = declarative_base(metadata=mymeta)


class State(Base):
    """ defines a class state"""
    __tablename__ = 'states'

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
