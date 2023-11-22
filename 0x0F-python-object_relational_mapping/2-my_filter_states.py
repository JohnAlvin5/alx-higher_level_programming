#!/usr/bin/python3
""" takes in an arguement and displays all values in the states table
    of the database hbtn_0e_0_usa """
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
    curs.execute("SELECT * FROM states WHERE BINARY name = '{}'".format(sys.argv[4]))
    for row in curs.fetchall():
        print(row)
