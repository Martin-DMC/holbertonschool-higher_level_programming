#!/usr/bin/python3
"""
in this module I define a script that make a query in sqlalchemy
where adds the State object 'Louisiana" to the database and display
the id of the states
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
    try:
        with Session() as session:
            new_state = State(name="Louisiana")
            session.add(new_state)
            session.commit()
            print(f"{new_state.id}")
    except Exception as e:
        print(f"Error: {e}")
