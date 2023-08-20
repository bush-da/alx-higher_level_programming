#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`")
    [print(state) for state in cur.fetchall()]
    cur.close()
    db.close()
