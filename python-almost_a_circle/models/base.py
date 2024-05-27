#!/usr/bin/python3
""" Class Base """


import json


class Base:
    """ Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ New instance of class Base """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns string representation of list_dictioonaries """
        if list_dictionaries is None or not list_dictionaries:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))
