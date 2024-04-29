#!/usr/bin/python3
"""Script that lists all State objects from the database"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    if len(sys.argv) == 4:
        # create an engine that connects to the MySQL Server
        engine = create_engine(
                "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                    sys.argv[1], sys.argv[2], sys.argv[3]))

        # Create a session maker bound to the engine
        Session = sessionmaker(bind=engine)

        # Create a session
        session = Session()

        # query the db to fetch all State objects and sort them by id
        states = session.query(State).order_by(State.id).all()

        # Display the results
        for state in states:
            print("{}: {}".format(state.id, state.name))

        # Close the session
        session.close()
