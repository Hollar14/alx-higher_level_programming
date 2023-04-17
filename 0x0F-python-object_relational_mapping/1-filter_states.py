#!/usr/bin/python3
"""
-- lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa:
-- Takes 3 arguments: mysql username, mysql password and 
database name (no argument validation needed)
-- Used the module MySQLdb (import MySQLdb)
-- Connects to a MySQL server running on localhost at port 3306
-- Results are sorted in ascending order by states.id
-- Code is not executed when imported
"""
import MySQLdb
import sys


if __name__ == "__main__":
    dtb = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cusr = dtb.cursor()
    cusr.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
    the_rows = cusr.fetchall()
    for row in the_rows:
        print(row)
    cusr.close()
    dtb.close()
