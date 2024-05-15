#!/usr/bin/python3
def roman_to_int(roman_string):
    nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0
    prev = 0
    if not isinstance(roman_string, str) or roman_string is None:
        return num
    for letter in reversed(roman_string):
        if letter in nums:
            value = nums[letter]
            if value < prev:
                num -= value
            else:
                num += value
            prev = value
    return num
