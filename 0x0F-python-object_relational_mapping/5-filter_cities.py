#!usr/bin/python3

"""
takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""

import MySQLdb as db
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    try:
        session = db.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                database=database
                )

        cursor = session.cursor()

        query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """
        cursor.execute(query, (state,))

        rows = cursor.fetchall()

        cities = ", ".join(city[0] for city in rows)
        print(cities)

    except db.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'session' in locals():
            session.close()
