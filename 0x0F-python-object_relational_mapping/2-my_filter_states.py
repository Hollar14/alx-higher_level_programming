#!/usr/bin/python3
"""
-- Takes 4 arguments: mysql username, mysql password, 
database name and state name searched
-- Used the module MySQLdb (import MySQLdb)
-- Connects to a MySQL server running 
on localhost at port 3306
-- Used format to create the SQL query with the user input
-- Results are sorted in ascending order by states.id
-- Code is not executed when imported
"""
import MySQLdb
import sys


if __name__ == "__main__":
    dtb = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cusr = dtb.cursor()
    cusr.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
   the_rows = cusr.fetchall()
    for row in the_rows:
        print(row)
    cusr.close()
    dtb.close()
