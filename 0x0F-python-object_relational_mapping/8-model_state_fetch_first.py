#!/usr/bin/python3
"""
-- prints the first State object from the database hbtn_0e_6_usa
-- Your script should take 3 arguments: mysql username, 
   mysql password and database name
-- You must use the module SQLAlchemy
-- You must import State and Base from model_state - 
   from model_state import Base, State
-- Your script should connect to a MySQL server running on 
   localhost at port 3306
-- The state you display must be the first in states.id
-- You are not allowed to fetch all states from the database 
   before displaying the result
-- The results must be displayed as they are in the example below
-- If the table states is empty, print Nothing followed by a new line
-- Your code should not be executed when imported
"""
import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    main_engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(main_engine)
    Session = sessionmaker(bind=main_engine)
    main_session = Session()
    instance = main_session.query(State).first()
    if instance is None:
        print("Nothing")
    else:
        print(instance.id, instance.name, sep=": ")
