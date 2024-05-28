#!/usr/bin/python3

""" Function that inherits for Mylist and creates a list of integers """


class Mylist(list):
        """ Creating the class Mylist that inherits from list """

        def print_sorted(self):
            """ Prints integers and sorts in order """

            print(sorted(self))
