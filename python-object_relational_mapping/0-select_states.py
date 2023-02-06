#!/usr/bin/python3
"""module documented"""
import sys
import MySQLdb


if __name__ = "__main__":
    dbconn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.curser()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query = cur.fetchall()
    for row in query:
        print(row)
    cur.close()
    dbconn.close()
