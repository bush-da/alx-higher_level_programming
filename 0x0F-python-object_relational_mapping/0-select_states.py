#!/usr/bin/python3
# script that lists all states from the database hbtn_0e_0_usa
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY `states`.`id`");
    [print(state) for state in c.fetchall()]
    c.close()
    db.close()
