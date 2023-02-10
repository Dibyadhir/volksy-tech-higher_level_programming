#!/usr/bin/python3
""" this is documented """
import sys
import MySQLdb


if __name__ == '__main__':
    con = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = con.cursor()
    cur.execute('''select cities from states inner join cities
            on state_id = states.id where states.name = x''')
    y = cur.fetchall()
    for i in y:
        print(i)
