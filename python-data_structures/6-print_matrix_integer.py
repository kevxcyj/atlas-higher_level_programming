#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for str in matrix:
        for i in str:
            if i == str[-1]:
                print('{:d}'.format(i), end='')
            else:
                print('{:d}'.format(i), end=' ')
        print()
