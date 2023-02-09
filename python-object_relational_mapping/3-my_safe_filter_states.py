#!/usr/bin/python3
""" this is ORM """
import MySQLdb
import os


if __name__ == '__main':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE Name = %s ORDER BY id,
            [sys.argv[4]')
    f = cur.fetchall()
    for i in f:
        print(i)
