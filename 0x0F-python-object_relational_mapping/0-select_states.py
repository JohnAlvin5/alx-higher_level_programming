#!/usr/bin/python3

""" Lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
            user = sys.argv[1],
            passwd = "Alvin254.5",
            db = sys.argv[3]
            )

    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM `states`")
    [print(state) for state in mycursor.fetchall()]
