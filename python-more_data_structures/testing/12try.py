#!/usr/bin/python3
def roman_to_int(roman_string):
    key = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0
    if not isinstance(roman_string, str) or roman_string is None:
        return num
    for i in range(len(roman_string)):
        if i + 1 < len(roman_string) and key[roman_string[i]] < key[roman_string[i + 1]]:
            num -= key[roman_string[i]]
        else:
            num += key[roman_string[i]]
    return num
