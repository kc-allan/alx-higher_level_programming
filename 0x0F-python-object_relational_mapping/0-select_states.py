#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
Usage: ./0-select_states.py <username> <password> <database name>
"""
import sys
import MySQLdb

args = sys.argv
dbuser = args[1]
dbpasswd = args[2]
dbname = args[3]
db = MySQLdb.connect(host="localhost", user=dbuser, port=3306, passwd=dbpasswd, db=dbname)
cur = db.cursor()
cur.execute("SELECT * FROM states")
rows = cur.fetchall()
for row in rows:
    print(row)