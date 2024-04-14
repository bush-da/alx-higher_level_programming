#!/usr/bin/python3
'''
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa '''
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    conn = MySQLdb.connect(user=username, passwd=password, db=database)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM `states` \
                    WHERE BINARY `name` = '{}'".format(sys.argv[4]))
    [print(state) for state in cursor.fetchall()]
