#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    s_dict = sorted(a_dictionary)
    for keys in s_dict:
        print(f"{keys}: {a_dictionary[keys]}")
