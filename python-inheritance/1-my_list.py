#!/usr/bin/python3

""" Function that inherits for Mylist and creates a list of integers """


class Mylist(list):
    """ Creating the class Mylist """

    def print_sorted(self):
            """ Prints integers and sorts in order """

            for i in self:
                if not isinstance(i, int):
                    raise TypeError()

            print(sorted(self))
