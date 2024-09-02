#!/usr/bin/python3

"""
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import MySQLdb as db
import sys

if __name__ == "__main__":
    session = db.connect(host="localhost", port=3306, user="root", passwd="MyZqe1", db="hbtn_0e_0_usa")
    cursor = session.cursor()

    arg = sys.argv[1]

    cursor.execute("SELECT * FROM states WHERE name = %s", (arg,))

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    session.close()
