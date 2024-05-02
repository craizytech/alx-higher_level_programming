#!/usr/bin/python3
"""Update a state object that has a specific id"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from model_state import Base, State
import sys


if __name__ == '__main__':
    # Create the database connection
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create a Session object and bind to the engine
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query the database
    state = session.query(State).filter(State.id == 2).first()

    # Change the name of the state to New Mexico
    state.name = "New Mexico"

    # Commit the Transaction
    session.commit()

    # Close the session out
    session.close()
