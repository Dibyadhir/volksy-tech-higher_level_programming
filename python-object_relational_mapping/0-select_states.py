#!/usr/bin/python3
""" module is documented """
import MySQLdb
import sys


if __name__ = "__main__":
    dbconn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query = cur.fetchall()
    for i in query:
        print(i)
    cur.close()
    dbconn.close()
