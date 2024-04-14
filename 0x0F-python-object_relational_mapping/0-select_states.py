#!/usr/bin/python3
import MySQLdb
import sys

def list_states(username, password, database_name):
    # connect to the database

    conn = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, database=database_name)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    database_name = sys.argv[3]

    list_states(username, passwd, database_name)
