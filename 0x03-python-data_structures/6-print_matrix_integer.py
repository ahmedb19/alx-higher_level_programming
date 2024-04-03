#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    else:
        for i in range(matrix):
            print("{:d} ".format(matrix[i]))
