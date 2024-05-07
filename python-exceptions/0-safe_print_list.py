#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    list_t = 1, 2, 3, 4
    try:
        for i in range(x):
            list_t(my_list[i], end='')
            list_t += 1
    except IndexError:
        pass
    finally:
        print()
        return list_t
