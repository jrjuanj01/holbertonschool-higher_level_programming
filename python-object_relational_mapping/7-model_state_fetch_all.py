#!/usr/bin/python3
"""Fetches states from dtatbase"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine 
from sqlalchemy.orm import session_maker


if __name__ == "__main__":
    """create engine"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = session_maker(bind=engine)
    session = Session
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(state)
    session.close()
