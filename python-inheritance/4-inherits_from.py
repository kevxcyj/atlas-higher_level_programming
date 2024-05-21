#!/usr/bin/python3

""" Defines inherits_from  """


def inherits_from(obj, a_class):

    """ Returns True if the object is an instance of
        a class that inherited from specific class """

    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    else:
        return False
