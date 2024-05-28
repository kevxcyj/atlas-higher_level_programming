#!/usr/bin/python3
""" Function that inherits for Mylist module and creates a list of integers """

MyList = __import__('1-my_list').MyList

class Mylist(list):
    """ Mylist class - that inherits from list """
    def print_sorted(self):
        """ Prints integers in Mylist and sorts in order """

        print(sorted(self))
