#!/usr/bin/python3
""" Script that prints the State object with the name passed as argument """


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

    state_name = argv[4]
    engine = create_engine(db)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).filter(State.name == state_name)
    rows = query.all()
    if (rows):
        for row in rows:
            print("{:d}".format(row.id))
    else:
        print("Not found")


if __name__ == "__main__":
    connect_mysql()
