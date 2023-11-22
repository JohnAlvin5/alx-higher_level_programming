#!/usr/bin/python3
""" takes in the name of a state as an argument and lists all cities
    of that state, using the database hbtn_0e_4_usa"""
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
    curs.execute("""
        SELECT cities.name FROM cities 
        INNER JOIN states 
        ON states.id=cities.state_id
        WHERE states.name=%s""", (sys.argv[4],)
        )
    city = curs.fetchall()
    city_list = list(row[0] for row in city)
    print(*city_list, sep=", ")
