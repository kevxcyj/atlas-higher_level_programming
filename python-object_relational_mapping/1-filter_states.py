#!/usr/bin/python3
""" Script that lists all states with a name starting with N """

import MySQLdb
from sys import argv


def connect_mysql():
    """Connect to MySQL server """
    db = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        host="localhost",
        port=3306
        )

    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states \
        WHERE name LIKE BINARY 'N%' \
        ORDER BY states.id ASC"
        )
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    connect_mysql()
