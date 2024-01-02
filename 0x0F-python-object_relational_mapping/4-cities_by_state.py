#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_0_usa
Usage: ./4-cities_by_state <username> <password> <database name>
"""
import MySQLdb
from sys import argv
if __name__ == '__main__':
    db = MySQLdb.connect(
		host='localhost',port=3306 ,user=argv[1], passwd=argv[2], db=argv[3]
	)
    cur = db.cursor()
    cur.execute("\
        SELECT cities.id, cities.name, states.name\
        FROM states\
        INNER JOIN cities ON states.id=cities.state_id")
    rows = cur.fetchall()
    for row in rows:
        print(row)