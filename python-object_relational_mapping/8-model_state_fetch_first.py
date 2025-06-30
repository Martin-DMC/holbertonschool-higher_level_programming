#!/usr/bin/python3
"""
in this module I define a script that make a query in sqlalchemy
where list only the first states of database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    with Session() as session:
        state = session.query(State).order_by(State.id).first()
        if state is None:
            print("Nothing")
        else:
            print(f"{state.id}: {state.name}")
