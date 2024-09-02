#!/usr/bin/python3
import MySQLdb as db
import sys

if __name__ == "__main__":
    session = db.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

    cursor = session.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    session.cilose()
