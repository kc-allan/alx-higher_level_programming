#!/usr/bin/python3
"""Fetches all State object from the database that contain letter 'a'
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sys import argv
if __name__ == '__main__':
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            argv[1], argv[2], argv[3]
        ), pool_pre_ping=True
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    session.add(State(name='Louisiana'))
    session.commit()
    new_id = session.query(State).filter_by(name='Louisiana').first().id
    print(new_id)
