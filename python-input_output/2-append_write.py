#!/usr/bin/python3
""" Defines append_write """


def append_write(filename="", text=""):
    """ Appends a string at the end of a text file """

    with open(filename, "a") as f:
        return f.write(text)
