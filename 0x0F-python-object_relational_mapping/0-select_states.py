#!/usr/bin/python3

"""
script that lists all states from the database hbtn_0e_0_usa:
"""
import sys
import MySQLdb as db


def connect_and_query() -> None:

    """Connects to the database and executes a query to select all states."""
    try:
        cnx = db.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        cursor = cnx.cursor(cursorclass=db.cursors.Cursor)
        cursor.execute('SELECT * FROM states ORDER BY `id` ASC;')
        states = cursor.fetchall()

        for state in states:
            print(state)
    except Exception as e:
        return (e)


if __name__ == "__main__":
    connect_and_query()
