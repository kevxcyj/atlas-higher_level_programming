#!/usr/bin/python3
"""Script that takes in the name of a state as an argument and lists all cities """


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
    with db.cursor() as cur:
        cur.execute(
            "SELECT cities.id, cities.name, states.name \ FROM cities \
            JOIN states \ ON cities.state_id = states.id \
            WHERE states.name LIKE BINARY %(state_name)s \
            ORDER BY cities.id ASC", {'state_name': argv[4]}
        )
        rows = cur.fetchall()
        if rows is not None:
            city_names = ", ".join([row[1] for row in rows])
            print(city_names)


if __name__ == "__main__":
    connect_mysql()