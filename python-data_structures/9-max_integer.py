#!/usr/bin/python3

def max_integer(my_list=[]):

    if len(my_list) == 0:
        return None

    result = my_list[0]

    for c in my_list:
        if c > result:
            result = c
    return result
