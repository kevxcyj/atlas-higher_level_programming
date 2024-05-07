#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    list_t = []

    for r in range(list_length):
        num = 0

        try:
            num = my_list_1[r] / my_list_2[r]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            
            print("out of range")
        except TypeError:

            print("wrong type")
        finally:
            list_t.append(num)

    return list_t
