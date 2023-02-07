#!/usr/bin/python3
""" this is documented """
import sys
import MySQLdb


if __name__ == '__main__':
    con = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cor = con.cursor()
    x = sys.argv[4]
    a = 'select * from states where name = {} order by id'.format(x)
    cur.execute(a)
    y = cur.fetchall()
    for i in y:
        print(i)
