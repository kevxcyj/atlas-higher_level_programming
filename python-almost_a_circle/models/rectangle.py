#!/usr/bin/python3
""" Inheriting from base.py """


from models.base import Base


class Rectangle(Base):
    """ Class Rectangle """

    def _init_(self, width, height, x=0, y=0, id=None):
        """ Attributes for rectangle
            width = width of rectangle
            height = height of rectangle """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
