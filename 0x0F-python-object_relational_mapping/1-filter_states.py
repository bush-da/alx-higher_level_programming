#!/usr/bin/python3
# List all states with a name starting with "N" from database hbtn_0e_0_usa

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states` WHERE name LIKE 'N%' ORDER BY states.id")
    [print(state) for state in c.fetchall()]
