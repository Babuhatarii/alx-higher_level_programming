#!/usr/bin/python3
"""
Script to list all states from a MySQL database.
"""

import MySQLdb
import sys


def list_states(username, password, database):
    """
    Connects to a MySQL database and lists all states.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.

    Returns:
        None
    """
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    connection.close()


if __name__ == "__main__":
    username, password, database = sys.argv[1:4]
    list_states(username, password, database)
