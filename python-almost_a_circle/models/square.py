#!/usr/bin/python3
""" Imports from rectangle.py """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ New instance """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns str format """
        return ("[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.width)
        )
    
    @property
    def size(self):
        """ Size of square """

        return self.width

    @size.setter
    def size(self, value):
        """ Validate value """

        self.width = value
        self.height = value
