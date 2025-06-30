#!/usr/bin/python3
"""
in this module I define a script that make a query in sqlalchemy
where lists all cities of database
"""
import sys
from model_state import Base, State
from model_city import City
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
            results = session.query(City, State)\
                      .join(State, City.state_id == State.id)\
                      .order_by(City.id).all()
            for city, state in results:
                print(f"{state.name}: ({city.id}) {city.name}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
