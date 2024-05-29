#!/usr/bin/python3
""" Function that inherits for Mylist module and creates a list of integers """


class Mylist(list):
    """
    Inherits from Python's built-in list class to create a specialized list for handling integers.

    Attributes:
        __init__: Initializes the Mylist object, inheriting from the list class.
        print_sorted: A method to sort the integers in the Mylist object and print them in ascending order.
    """
    def print_sorted(self):
        """ Prints integers in Mylist and sorts in order """

        print(sorted(self))