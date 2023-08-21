#!/usr/bin/python3
""" lists all states with a name starting with N from the database """
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    curr = db.cursor()
    curr.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in curr.fetchall() if state[1][0] == "N"]
