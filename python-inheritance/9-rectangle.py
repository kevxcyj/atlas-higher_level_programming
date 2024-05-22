#!/usr/bin/python3
""" Imports 7-base_geometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Writes a class Rectangle that inherits from 7-base_geometry.py """

    def __init__(self, width, height):
        """ Validator """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        """ Return """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
