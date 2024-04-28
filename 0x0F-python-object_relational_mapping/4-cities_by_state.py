#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_0_usa."""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) == 4:
        db = MySQLdb.connect(
                host="localhost",
                user=sys.argv[1],
                password=sys.argv[2],
                db=sys.argv[3],
                port=3306)

    cursor = db.cursor()

    # fetch all the states from the database
    cursor.execute("SELECT cities.id, cities.name, states.name\
                   FROM cities\
                   INNER JOIN states\
                   ON cities.state_id = states.id\
                   ORDER BY cities.id")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
