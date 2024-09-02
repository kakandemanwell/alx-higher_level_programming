#!/usr/bin/python3

"""
Lists all State objects'
that contain the letter a from the database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
import sys

if __name__ == "__main__":
    """
    connects to database parsed and filters and lists a stste containing a.
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%'))

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
