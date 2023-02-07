#!/usr/bin/python3
""" module is documented """
import MySQLdb
import sys


if __name__ == "__main__":
    con = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = con.cursor()
    q = 'select * from states order by id'
    cur.execute(q)
    a = cur.fetcthall()
    for i in a:
        print(i)
