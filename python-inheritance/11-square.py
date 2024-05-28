#!/usr/bin/python3

""" Class Square """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Defines square based on 10-square.py """
    def __init__(self, size):

        """ Size = length """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return (self.__size ** 2)

    def __str__(self):
        """ Prints and returns str """

        return ("[Square] {}/{}".format(self.__size, self.__size))
