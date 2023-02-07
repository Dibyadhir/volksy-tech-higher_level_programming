#!/usr/bin/python3
""" this is documented """
import sys
import MySQLdb


if __name__ == '__main__':
    con = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cor = con.cursor()
    x = sys.argv[4]
    a = 'select * from states where binary name = "{}" order by id'.format(x)
    cor.execute(a)
    y = cor.fetchall()
    for i in y:
        print(i)
