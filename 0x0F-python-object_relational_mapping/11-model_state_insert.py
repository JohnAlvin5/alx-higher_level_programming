#!/usr/bin/python3
""" adds the State object "Louisiana" to the database hbtn_0e_6_usa."""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    loui = State(name="Louisiana")
    session.add(loui)
    session.commit()
    print(loui.id)
