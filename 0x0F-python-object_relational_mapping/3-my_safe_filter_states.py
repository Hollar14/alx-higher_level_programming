#!/usr/bin/python3

"""
-- Takes in arguments and displays all values in the states table 
of hbtn_0e_0_usa where name matches the argument
-- Your script should take 4 arguments: mysql username, mysql password, 
database name and state name searched (safe from MySQL injection)
-- You must use the module MySQLdb (import MySQLdb)
-- Your script should connect to a MySQL server running on localhost at port 3306
-- Results must be sorted in ascending order by states.id
-- Your code should not be executed when imported
"""

import MySQLdb
import sys


if __name__ == "__main__":
    dtb = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cusr = dtb.cursor()
    match_found = sys.argv[4]
    cusr.execute("SELECT * FROM states WHERE name LIKE %s", (match_found, ))
    the_rows = cusr.fetchall()
    for row in the_rows:
        print(row)
    cusr.close()
    dtb.close()
