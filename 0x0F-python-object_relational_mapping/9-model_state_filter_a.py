#!/usr/bin/python3
"""Lists all state objects containing the letter 'a'"""
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
    states = session.query(State).order_by(State.id).all()

    # Print the states according to the requirements
    for state in states:
        if 'a' in state.name:
            print("{}: {}".format(state.id, state.name))

    # Close the session out
    session.close()
