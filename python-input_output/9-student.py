#!/usr/bin/python3
""" Class Student """


class Student:
    """ Defines a student by Public instance attributes """

    def __init__(self, first_name, last_name, age):
        """ Instance attributes """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieves student representation """

        return (self.__dict__)
