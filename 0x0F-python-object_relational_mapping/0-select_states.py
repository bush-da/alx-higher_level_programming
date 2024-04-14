#!/usr/bin/python3
# List all states from the database
import sys
import MySQLdb

if __name__ == "__main__":
    try:
        conn = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM `states` ORDER BY `states`.`id`")

        [print(state) for state in cursor.fetchall()]

        cursor.close()
        conn.close()

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
        sys.exit(1)
