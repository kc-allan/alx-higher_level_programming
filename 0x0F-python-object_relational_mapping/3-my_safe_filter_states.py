#!/usr/bin/python3
"""
Script that lists all states with a name starting with N
Usage: ./1-filter_states.py <MySQL username> <MySQL password> <database_name>
"""
from sys import argv
import MySQLdb
if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost', port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )
    cur = db.cursor()
    query = "SELECT * FROM states WHERE states.name = %s"
    input = argv[4]
    cur.execute(query, (input,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
