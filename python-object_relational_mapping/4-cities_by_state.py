#!/usr/bin/python3
""" this is ORM """
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],passwd=sys.argv[2],db=sys.argv[3])
    cur = db.cursor()
    cur.execute('select cities.id, cities.name, state.name from states inner join cities on cities.state_id = states.id order by id')
    y = cur.fetchall()
    for i in y:
        print(i)
