#!/usr/bin/python3
def square_matrix_map(mat):
    return list(map(lambda a: list(map(lambda x: x ** 2, a)), mat))
