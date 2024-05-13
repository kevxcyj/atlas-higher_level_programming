#!/usr/bin/python3
""" A function that prints a quare with the character # """


def print_square(size):
    """ Function """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    

    if size < 0:
        raise ValueError("size must be >= 0")


    for r in range(size):
        [print("#", end="") for i in range(size)]
        print("")
