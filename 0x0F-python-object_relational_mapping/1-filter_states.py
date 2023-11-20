#!/usr/bin/python3

"""Lists all states with a name starting with upper N from the
    database hbtn_0e_0_usa."""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )

    curs = db.cursor()
    curs.execute("SELECT * FROM `states` WHERE name LIKE BINARY 'N%' ORDER BY `id`")
    for row in curs.fetchall():
            print(row)
