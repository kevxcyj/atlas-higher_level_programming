#!/usr/bin/python3
""" Sctipt that takes in an argument and displays all values in the states table of hbtn_0e_0_usa """


from sys import argv
import MySQLdb


def connect_mysql():
    """Connect to a MySQL server """
    db = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        host="localhost",
        port=3306
        )

    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states \ WHERE name LIKE BINARY '{}' \
        ORDER BY states.id ASC".format(argv[4])
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    connect_mysql()
