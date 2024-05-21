#!/usr/bin/python3

""" Class that inherits from list """



class Mylist(list):

    """ Defines print_sorted """


    def print_sorted(self):

        for s in self:
            if not isinstance(s, int):
                raise TypeError()
            
        print(sorted(self))
