#!/usr/bin/python3
import MySQLdb as db
import sys

"""
 takes in arguments and displays all values in the states
 table of hbtn_0e_0_usa where name matches the argument
"""

if __name__ == "__main__":
    if len (sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password> <database name> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        session = db.connect(host="localhost",
                port=3306,
                user=username,
                passwd=password,
                database=database,
                charset="utf8"
                )

        cursor = session.cursor()

        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

        cursor.execute(query, (state_name,))

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except db.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)

    finally:
        cursor.close()
        session.close()
