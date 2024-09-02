#usr/bin/python3
import MySQLdb as db
import sys

"""
lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
        """

        cursor.execute(query)

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except db.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'session' in locals():
            session.close()
