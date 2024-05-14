#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list[:]
    for idx in range(0, len(my_list)):
        if my_list[idx] % 2 == 0:
            new_list[idx] = True
        else:
            new_list[idx] = False
    return new_list
