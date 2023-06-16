#!/usr/bin/python3
# List all states from database hbtn_0e_0_usa
# Usage: ./0-select_states.py <mysql username> \
#                              <mysql password> \
#                              <database name>
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    p = db.cursor()
    p.execute("SELECT * FROM `states`")
    [print(state) for state in p.fetchall()]
