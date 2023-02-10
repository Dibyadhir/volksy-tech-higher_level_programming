#!/usr/bin/python3
""" this is documented """
import sys
import MySQLdb


if __name__ == '__main__':
    con = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = con.cursor()
    x = sys.argv[4]
    cur.execute('''select cities.name from states inner join cities
            on state_id = states.id where states.name = '{}' '''.format(x))
    y = cur.fetchall()
    if len(y) == 0:
        print()
    else:
        for i in range(len(y)):
            if len(y) - 1 == i:
                print(y[i][0])
            else:
                print(y[i][0], end=", ")
