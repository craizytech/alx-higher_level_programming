#!/usr/bin/python3
"""Script that insert an object to the database"""
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

        # create the state
        state = State(name="Louisiana")
        session.add(state)

        # Commit it to the session
        session.commit()

        # Query the database for the states
        state = session.query(State).filter(State.name == 'Louisiana').first()

        # Display the results
        if state:
            print(state.id)
        else:
            print("Nothing")

        # Close the session
        session.close()
