#!/usr/bin/python3
"""
in this module I define a script that make a query in sqlalchemy
where i delete all states that contain 'a' in there name of database
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
            states = session.query(State).filter(State.name.like('%a%'))\
                    .delete()
            session.commit()
    except Exception as e:
        print(f"Error: {e}")
