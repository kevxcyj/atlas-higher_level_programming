#!/usr/bin/python3

""" Defines Rectangle """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Defines rectangle based on 7-base_geometry """

    def __init__(self, width, height):
        """ Width(Horizontal) and Height(Vertical) """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
