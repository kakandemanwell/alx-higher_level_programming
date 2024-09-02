#!/usr/bin/python3
"""
prints all City objects from the database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>"\
                .format(sys.argv[0]))
        sys.exit(1)

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State.name)\
            .join(State, City.state_id == State.id)\
            .order_by(City.id).all()

    for city, state_name in cities:
        print("{}: ({}) {}".format(state_name, city.id, city.name))

    session.close()
