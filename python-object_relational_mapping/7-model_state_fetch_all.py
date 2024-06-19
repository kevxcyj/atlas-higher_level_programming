#!/usr/bin/python3
""" Script that lists all State objects from the database """


from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base
from model_state import State


def connect_mysql():
    """Connect to a MySQL server """
    db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1],
        argv[2],
        argv[3]
    )

    engine = create_engine(db)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).order_by(State.id)
    rows = query.all()
    for row in rows:
        print("{:d}: {:s}".format(row.id, row.name))


if __name__ == "__main__":
    connect_mysql()
