#!/usr/bin/python3
"""First state model"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """Base class for the states table"""
    __tablename__ = "states"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(128), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"{self.id} {self.name}"
