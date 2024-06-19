#!/usr/bin/python3
""" Script that """

from sys import argv
import MYSQLdb


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
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    connect_mysql()
