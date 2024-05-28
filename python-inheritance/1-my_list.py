#!/usr/bin/python3
""" Function that inherits for Mylist and creates a list of integers """


class Mylist(list):
    """ Creating th class Mylist """

    def print_sorted(self):
        """ Prints integers and sorts """

        for i in self:
            if not isinstance(i, int):
                raise TypeError()

        print(sorted(self))
