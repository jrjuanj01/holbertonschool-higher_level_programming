#!/usr/bin/python3
def roman_to_int(roman_string):
    numeral_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0
    if not isinstance(roman_string, str) or roman_string is None:
        return num
    for letter, next_letter in zip(roman_string, roman_string[1:]):
        if letter in numeral_dict:
            if next_letter is None:
                num += numeral_dict[letter]
            else:
                if numeral_dict[next_letter] > numeral_dict[letter]:
                    num -= numeral_dict[letter]
                else:
                    num += numeral_dict[letter]
    return num
