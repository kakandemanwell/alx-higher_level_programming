#!/usr/bin/python3

"""
Lists a State object,
with the same name as the passed argument from the database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
import sys

if __name__ == "__main__":
    """
    connects to database parsed and filters and lists a stste passed.
    """
    state_name = sys.argv[4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name == state_name)
    for state in states:
        if state.name == state_name:
            print("{}: {}".format(state.id, state.name))
    else:
        print("Not found")
    session.close()
