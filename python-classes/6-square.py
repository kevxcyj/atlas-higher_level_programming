#!/usr/bin/python3
""" Writes a class square that defines a square """


class Square:
    """ Function """

    def __init__(self, size=0, position=(0,0)):
        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()

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
        s_position = ""
        if self.size == 0:
            return "\n"
        
        for n in range(self.position[1]):
            s_position += "\n"
        for n in range(self.size):
            for x in range(self.position[0]):
                s_position += " "
            for y in range(self.size):
                s_position += "#"

            s_position += "\n"

        return s_position
    
    def my_print(self):
        print(self.positive_p(), end='')
