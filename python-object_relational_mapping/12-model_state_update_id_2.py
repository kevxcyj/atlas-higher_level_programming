#!/usr/bin/python3
"""Script that changes the name of a State object """


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
    update_id = 2
    new_name = "New Mexico"
    rows = session.query(State).filter(State.id == update_id)
    for row in rows:
        row.name = new_name
    session.commit()
    session.close()


if __name__ == "__main__":
    connect_mysql()
