#!/usr/bin/python3
''' script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa '''
import sys
import MySQLdb

if __name__ == "__main__":
    host = 'localhost'
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
    c = db.cursor()
    c.execute('SELECT * FROM `states` ORDER BY `states`.`id`')
    [print(state) for state in c.fetchall() if state[1][0] == "N"]
    c.close()
    db.close()
