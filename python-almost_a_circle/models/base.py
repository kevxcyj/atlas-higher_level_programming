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

    @classmethod
    def save_to_file(cls, list_objs):
        """ Returns string representation of list_objs """
        if list_objs is None:
            list_objs = []

        filename = f"{cls.__name__}.json"
        with open(filename, "w") as file:
            json_string = (cls.to_json_string([obj.to_dictionary()
                                               for obj in list_objs]))

            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """ Returns string representation of json_string """
        if json_string is None or not json_string:
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ Returns instance with attributes already set """
        tmp_obj = cls(1, 1)
        tmp_obj.update(**dictionary)
        return tmp_obj

    @classmethod
    def load_from_file(cls):
        """ Returns list of instances """
        file_name = f"{cls.__name__}.json"
        try:
            with open(file_name, "r") as file:
                return (([cls.create(**data) for
                          data in cls.from_json_string(file.read())]))
        except FileNotFoundError:
            return ([])
