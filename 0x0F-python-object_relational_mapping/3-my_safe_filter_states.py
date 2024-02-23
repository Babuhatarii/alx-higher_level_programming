#!/usr/bin/python3
"""
script that takes in arguments and displays all
values in the states table of hbtn_0e_0_usa
"""
import sys
import MySQLdb as db


def connect_and_query() -> None:

    """Connect to the database and execute query"""
    try:
        cnx = db.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        cursor = cnx.cursor(cursorclass=db.cursors.Cursor)
        cursor.execute("SELECT * FROM states WHERE name = %s \
                        ORDER BY id ASC;", (sys.argv[4], ))
        states = cursor.fetchall()

        for state in states:
            if state[1] == sys.argv[4]:
                print(state)
    except Exception as e:
        return (e)


if __name__ == "__main__":
    connect_and_query()
