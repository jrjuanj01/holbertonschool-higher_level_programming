#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for idx in range(0, x):
            print("{}".format(my_list[idx]), end= "" if idx < x - 1 else "\n")
        digit = idx + 1
    except IndexError:
        for idx in range(0,):
            print("{}".format(my_list[idx]), end= "")
        print()
        digit = idx
    return digit
