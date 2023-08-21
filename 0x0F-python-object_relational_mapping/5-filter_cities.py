#!/usr/bin/python3
"""  script that takes in the name of a state as an argument
 and lists all cities of that state, using the database hbtn_0e_4_usa """

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curr = db.cursor()
    query = "SELECT * FROM `cities` INNER JOIN `states` ON \
             `cities`.`state_id` = `states`.`id` ORDER BY `cities`.`id`"
    curr.execute(query)
    print(", ".join([c[2] for c in curr.fetchall() if c[4] == sys.argv[4]]))
