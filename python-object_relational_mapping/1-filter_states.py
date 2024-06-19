/usr/bin/python3
""" Script that lists all states with a name starting with N """

import MySQLdb
from sys import argv


def connect_mysql():
    """Connect to MySQL server """
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

     cur = db.cursor()
    nmeSr = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])
    cur.execute(nmeSr)

    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    db.close()

if __name__ == '__main__':
    connect_mysql()
