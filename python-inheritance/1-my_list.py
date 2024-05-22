#!/usr/bin/python3
""" Function """


class Mylist(list):
    """ Class MyList """


    def print_sorted(self):
        """ Prints integers """

        for s in self:
            if not isinstance(s, int):
                raise TypeError()
            
        print(sorted(self))
