#!/usr/bin/python3
"""Fetches cities from dtatbase"""
from model_state import Base, State
from model_city import City
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 file.py username password database")
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).join(State).order_by(City.id).all()
    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")
    session.close()
