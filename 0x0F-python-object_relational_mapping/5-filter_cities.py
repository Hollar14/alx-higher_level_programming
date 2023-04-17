#!/usr/bin/python3
"""  
-- takes in the name of a state as an argument and lists all 
   cities of that state, using the database hbtn_0e_4_usa
-- Your script should take 4 arguments: mysql username, mysql password, 
   database name and state name (SQL injection free!)
-- You must use the module MySQLdb (import MySQLdb)
-- Your script should connect to a MySQL server running on localhost 
   at port 3306
-- Results must be sorted in ascending order by cities.id
-- You can use only execute() once
-- Your code should not be executed when importedlists all states 
   from the database hbtn_0e_0_usa 
"""
import MySQLdb
import sys


if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cusr = database.cursor()
    cusr.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    the_rows = cusr.fetchall()
    temporary = list(row[0] for row in the_rows)
    print(*temporary, sep=", ")
    cusr.close()
    database.close()
