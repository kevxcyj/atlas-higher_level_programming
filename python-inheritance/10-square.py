#!/usr/bin/python3
""" Imports 9-rectangle.py """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Writes a class square that inherits from 9-rectangle.py """

    def __init__(self, size):
        """ Validator """

        if self.integer_validator('size', size):
            self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Returns area of Square object"""
        return super().area()
