#!/usr/bin/python3
"""
Takes state as an argument an prints out its cities from the database
Usage: ./5-filter_cities <username> <password> <database name> <state name>
"""
import MySQLdb
from sys import argv
if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost', port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )
    cur = db.cursor()
    state = argv[4]
    query = "SELECT cities.name\
        FROM states\
        INNER JOIN cities ON states.id=cities.state_id\
        WHERE states.name=%s"
    cur.execute(query, (state,))
    rows = cur.fetchall()
    for row in range(len(rows)):
        try:
            if row+1 == len(rows):
                print(rows[row][0])
            else:
                print(rows[row][0], end=', ')
        except IndexError:
            continue
