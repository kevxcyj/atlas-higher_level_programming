#!/usr/bin/python3

""" Defines class BaseGeometry base on 6-base.geometry """


class BaseGeometry:
    """ Raises exception """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Checks if the value is an integer is greater than zero """

        """ Return if not an integer """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
