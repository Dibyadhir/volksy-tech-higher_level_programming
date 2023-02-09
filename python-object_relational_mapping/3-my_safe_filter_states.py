#!/usr/bin/python3
""" this is ORM """
import MySQLdb
import os


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute('SELECT * FROM states')
    f = c.fetchall()
    for i in f:
        if i[1] == sys.argv[4]:
            print(i)
