#!/usr/bin/python3
def print_matrix_integer(matrix):
    for i in range(len(matrix)):
        if matrix[i] == 0:
            print("{:d}".format(""))
        for j in matrix[i]:
            if j == matrix[i][-1]:
                print("{:d}".format(j))
            else:
                print("{:d}".format(j), end=" ")
