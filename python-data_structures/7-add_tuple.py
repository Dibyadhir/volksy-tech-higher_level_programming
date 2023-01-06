#!/usr/bin/python3
def add_tuple(t1, t2):
    if len(t1) > 2:
        t1 = t1[:2]
    elif len(t1) == 1:
        t1 = tuple((t1[0], 0))
    elif len(t1) == 0:
        t1 = tuple((0, 0))
    a, b = t1
    if len(t2) > 2:
        t2 = t2[:2]
    elif len(t2) == 1:
        t2 = tuple((t2[0], 0))
    elif len(t2) == 0:
        t2 = tuple((0, 0))
    c, d = t2
    return tuple((a + c, b + d))
