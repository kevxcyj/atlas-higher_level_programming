#!/usr/bin/python3
""" Class Student """


class Student:
    """ Writes a class Student that defines student by 10-student.py """

    def __init__(self, first_name, last_name, age):
        """ Instance attributes """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves student representation """

        if (
            isinstance(attrs, list)
            and all(isinstance(attr, str) for attr in attrs)
        ):
            return {
                attr: getattr(self, attr) for attr in attrs
                if hasattr(self, attr)
            }

        return (self.__dict__)

    def reload_from_json(self, json_data):
        """ Replaces attributes """

        for key, value in json_data.items():
            setattr(self, key, value)
