#!/usr/bin/python3
"""
in this module I define a script that make a query in sqlalchemy
where i updating the name of the state with id=2 of database
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
            state = session.query(State).filter_by(id=2).first()
            state.name = "New Mexico"
            session.commit()
    except Exception as e:
        print(f"Error: {e}")
