#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max = my_list[0]
    for nums in my_list:
        if nums > max:
            max = nums
    return max
