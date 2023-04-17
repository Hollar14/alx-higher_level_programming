#!/usr/bin/python3

"""
-- lists all State objects from the database hbtn_0e_6_usa
-- Your script should take 3 arguments: mysql username, 
   mysql password and database name
-- You must use the module SQLAlchemy
-- You must import State and Base from model_state - from 
   model_state import Base, State
-- Your script should connect to a MySQL server running on 
   localhost at port 3306
-- Results must be sorted in ascending order by states.id
-- Your code should not be executed when imported
-- Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")
