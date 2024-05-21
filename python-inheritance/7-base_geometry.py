#!/usr/bin/bash

""" Defines class BaseGeometry """


class BaseGeometry:
    """ Raises exception """
    def area(self):

        raise Exception("area() is not implemented")
    
def integer_validator(self, name, value):
    """ Checks if the value is an integer is greater than zero """

    """ Return if not an integer """

    if type(value) is not int:
        raise TypeError(f"{name} must be an integer")
    if value <= 0:
        raise ValueError(f"{name} must be greater than 0")
