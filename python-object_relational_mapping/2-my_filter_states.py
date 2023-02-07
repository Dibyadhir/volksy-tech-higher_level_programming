#!/usr/bin/python3
""" module is documented """
import MySQLdb
import sys



if __name__ = "__main__":
    dbconn = MySQLdb.connect(host="localhost", port=3306, 
            user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = dbconn.cursor()
    x = sys.argv[4]
    a = 'select * from states where name = {} order by id'.format(x)
    cur.execute(a)
    y = cur.fetchall()
    for i in y:
        print(i)
