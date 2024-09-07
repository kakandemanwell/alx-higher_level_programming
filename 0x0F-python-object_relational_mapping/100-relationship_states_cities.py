#!/usr/bin/python3

"""
creates the State “California” with the City “San Francisco” from the database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City
import sys

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format
                           (sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cali = State(name="California")

    san = City(name="San Francisco", state=cali)

    session.add(cali)
    session.add(san)
    session.commit()

    session.close()
