#!/usr/bin/python3
"""Fetches City objects from the databse"""
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            argv[1], argv[2], argv[3]
        ), pool_pre_ping=True
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    cities = session.query(
        State.name, City.id, City.name
        ).join(
            State, State.id == City.state_id
            ).all()
    for state_name, city_id, city_name in cities:
        print("{}: ({}) {}".format(
            state_name, city_id, city_name
        ))
