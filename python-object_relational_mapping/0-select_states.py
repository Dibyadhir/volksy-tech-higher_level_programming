#!/usr/bin/python3
"""module documented"""
import sys
import MySQLdb


if __name__ = "__main__":
    db = MyAQLdb.connect(user=sys.argv[1],passwd=sys.argv[2],db=sys.argv[3])
    conn = db.cursor()
    conn.execute("SELECT * FROM ststes")
    [print(state) for state in conn.fetchall()]
