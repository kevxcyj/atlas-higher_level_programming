#!/usr/bin/python3

""" Defines is_kind_of_class  """


def is_kind_of_class(obj, a_class):
    """ Checks if object is and instance of, or if the object 
    is an instance of a class that inherited from """

    return isinstance(obj, a_class)
