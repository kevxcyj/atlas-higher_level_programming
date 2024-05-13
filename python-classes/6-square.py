#!/usr/bin/python3
""" Writes a class square that defines a square """


class Square:
    """ Function """

    def __init__(self, size=0, position=(0,0)):
        self.size = size
        self.position = position

    def __str__(self):
        self.print_sq()

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        
        if value < 0:
            raise ValueError('size must be >= 0')
        
        self.__size = value

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([v for v in value if isinstance(v, int) and v >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value

    def area(self):
        return self.__size ** 2

    def positive_p(self):
        s_positive = ""
        if self.size == 0:
            return "\n"
        
        for n in range(self.positive[1]):
            s_positive += "\n"
        for n in range(self.size):
            for x in range(self.positive[0]):
                s_positive += " "
            for y in range(self.size):
                s_positive += "#"

            s_positive += "\n"

        return s_positive
    
    def print_sq(self):
        print(self.positive_p(), end='')
