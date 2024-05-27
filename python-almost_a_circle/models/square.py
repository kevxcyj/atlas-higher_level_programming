#!/usr/bin/python3
""" Imports from rectangle.py """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ """
    def __init__(self, size, x=0, y=0, id=None):
        """ """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns str format """
        return ("[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.width)
        )
