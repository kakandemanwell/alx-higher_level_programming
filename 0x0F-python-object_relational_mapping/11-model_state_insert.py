#!/usr/bin/python3

"""
Adds a State object,
with the same name as the passed argument from the database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys

if __name__ == "__main__":
    """
    connects to database, adds the passed state.
    """

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    state_name = State(name=sys.argv[4])

    session.add(state_name)
    session.commit()

    print(state_name.id)
    session.close()
