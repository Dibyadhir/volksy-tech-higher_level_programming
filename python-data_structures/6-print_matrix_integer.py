#!/usr/bin/python3
def print_matrix_integer(matrix):
    for i in range(len(matrix)):
        if matrix[i] == 0:
            print()
        for j in matrix[i]:
            if j == matrix[i][-1]:
                print(j)
            else:
                print(j, end=" ")
