#!/usr/bin/python3
""" this is ORM """
import MySQLdb
import sys


if __name__ == '__main__':
    con = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cor = con.cursor()
    x = sys.argv[4]
    cor.execute('select * from states order by id')
    y = cor.fetchall()
    for i in y:
        if i[1] == x:
            print(i)
