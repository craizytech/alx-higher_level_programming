#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa."""
import MySQLdb;
import sys

if len(sys.argv) == 4:
    db = MySQLdb.connect(host="localhost:3306", user=sys.argv[1],\
            password=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()

    # fetch all the states from the database
    cursor.execute("SELECT id, name FROM states")
    rows = cursor.fetchall()
    
    for row in rows:
            print(row)
