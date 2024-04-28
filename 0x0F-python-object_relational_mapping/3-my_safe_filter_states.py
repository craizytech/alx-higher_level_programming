#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa and filter for states
where the name matches the last argument provided This script should be
safe from mysql injections"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) == 5:
        db = MySQLdb.connect(
                host="localhost",
                user=sys.argv[1],
                password=sys.argv[2],
                db=sys.argv[3],
                port=3306)

    cursor = db.cursor()

    # fetch all the states from the database

    query = "SELECT id, name FROM states WHERE BINARY name = %s ORDER BY id"
    args = (sys.argv[4],)
    cursor.execute(query, args)
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    cursor.close()
    db.close()
