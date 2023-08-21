#!/usr/bin/python3
""" script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections! """

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curr = db.cursor()
    query = "SELECT * FROM `states` \
             WHERE BINARY `name` = %s ORDER BY `id`"
    params = (sys.argv[4],)
    curr.execute(query, params)
    [print(state) for state in curr.fetchall()]
