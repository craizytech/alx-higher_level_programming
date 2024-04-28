#!/usr/bin/python3
"""lists cities in a state from the database hbtn_0e_0_usa by the state name"""
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
    cursor.execute("SELECT cities.name\
                   FROM cities\
                   INNER JOIN states\
                   ON cities.state_id = states.id\
                   WHERE states.name = %s\
                   ORDER BY cities.id", (sys.argv[4],))
    rows = cursor.fetchall()

    # make the output a comma separated string
    cities = ", ".join([row[0] for row in rows])
    print(cities)

    cursor.close()
    db.close()
