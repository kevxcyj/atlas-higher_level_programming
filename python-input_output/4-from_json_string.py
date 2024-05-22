#!/usr/bin/python3
""" Imports json, Defines from_json_string """


import json


def from_json_string(my_str):
    """ Returns an object represented by JSON string """

    return (json.loads(my_str))
