#!/usr/bin/python3
""" Defines write_file """


def write_file(filename="", text=""):
    """ Writes a string to a text file and returns
        the number of characters writen """

    with open(filename, "w") as f:
        return (f.write(text))
