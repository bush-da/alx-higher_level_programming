#!/usr/bin/python3
''' script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument. '''
import sys
import MySQLdb

if __name__ == '__main__':
    host = 'localhost'
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    name = sys.argv[4]
    db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
    c = db.cursor()
    c.execute('SELECT * FROM `states` ORDER BY `states`.`id`')
    [print(state) for state in c.fetchall() if name == state[1]]
    c.close()
    db.close()
