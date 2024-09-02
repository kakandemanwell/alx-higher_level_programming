#!/usr/bin/python3
import MySQLdb as db
import sys

if __name__ == "__main__":

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    session = db.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=database_name, charset="utf8")

    cursor = session.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    session.close()
