#!/usr/bin/python3
""" this is documented """
import sys
import MySQLdb


if __name__ == '__main__':
    conn = MySQLdb(sys.argv[1], sys.argv[2], db=sys.argv[3])
    cor = conn.cursor()
    v = 'select * from states where name like "N%" order by id'
    cor.execute(v)
    f = cor.fetchall()
    for i in f:
        if i[1].istitle():
            print(i)
