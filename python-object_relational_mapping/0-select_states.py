#!/usr/bin/python3
""" module is documented """
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    q = 'select * from states order by id'
    cur.execute(q)
    a = cur.fecthall()
    for i in a:
        print(i)
