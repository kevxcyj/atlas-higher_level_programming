#!/usr/bin/python3

""" Function that inherits for Mylist module and creates a list of integers """


class Mylist(list):
    """ Mylist class - that inherits from list """
    def print_sorted(self):
        """ Prints integers and sorts in order """

        print(sorted(self))
