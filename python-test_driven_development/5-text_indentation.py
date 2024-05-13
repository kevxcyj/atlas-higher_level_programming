#!/usr/bin/python3
""" Function that prints a text with 2 new lines after each of these characters """

def text_indentation(text):
    """ Function """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    space = ""
    for char in text:
        space += char
        if char in ['.', '?', ':']:
            print(space)
