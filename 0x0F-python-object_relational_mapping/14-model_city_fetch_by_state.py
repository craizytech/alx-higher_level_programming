#!/usr/bin/python3
"""Cities in States"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == '__main__':

    # Create engine to handle database connections
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create a sessionmaker object
    Session = sessionmaker(bind=engine)

    # Create a session object
    session = Session()

    # Query both cities and states
    cities = session.query(City).join(State).order_by(City.id).all()

    # Print the results
    for city in cities:
        print(f"{city.state.name}, {city.id}, {city.name}")

    # close the session out
    session.close()
