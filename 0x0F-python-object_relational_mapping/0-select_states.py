#!/usr/bin/python3
# List all states from the database
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(user=username, passwd=password, db=database)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM states ORDER BY states.id")

    [print(state) for state in cursor.fetchall()]
