#!/usr/bin/python3
""" Defines read_file """



def read_file(filename=""):
    """ Reads UTF8 file and prints to stdout """

    with open(filename) as f:
        print(f.read(), end="")
