#!/usr/bin/python3
""" Class that inherits from list """


class Mylist(list):
    """ Class MyList """


    def print_sorted(self):
        """ Prints integers """

        for s in self:
            if not isinstance(s, int):
                raise TypeError()
            
        print(sorted(self))
