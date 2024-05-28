#!/usr/bin/python3
""" Function that inherits for Mylist module and creates a list of integers """

class Mylist(list):
    """ Mylist class - that inherits from list 
        python3 -c "d = __import__(\"1-my_list\").MyList.__doc__ """
    def print_sorted(self):
        """ Prints integers and sorts in order """

        print(sorted(self))
