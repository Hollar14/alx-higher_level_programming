#!/usr/bin/python3
"""
-- lists all cities from the database hbtn_0e_4_usa
-- Your script should take 3 arguments: mysql username, 
   mysql password and database name
-- You must use the module MySQLdb (import MySQLdb)
-- Your script should connect to a MySQL server running 
   on localhost at port 3306
-- Results must be sorted in ascending order by cities.id
-- You can use only execute() once
-- Your code should not be executed when imported 
"""
import MySQLdb
import sys


if __name__ == "__main__":
    dtb = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cusr = dtb.cursor()
    cusr.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    the_rows = cusr.fetchall()
    for row in the_rows:
        print(row)
    cusr.close()
    dtb.close()
