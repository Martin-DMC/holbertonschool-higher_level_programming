#!/usr/bin/python3
"""
in this module I define a script that make a query in sqlalchemy
where display the id of the states that to match with searching of database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    state_to_search = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    try:
        with Session() as session:
            states = session.query(State).where(State.name == state_to_search)\
                    .order_by(State.id).all()
            if not states:
                print("Not found")
            else:
                for state in states:
                    print(f"{state.id}")
    except Exception as e:
        print(f"Error: {e}")
