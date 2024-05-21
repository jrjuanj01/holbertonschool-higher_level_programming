#!/usr/bin/python3
"""Prints name"""


def say_my_name(first_name, last_name=""):
    """Print function"""

    fn_err = "first_name must be a string"
    ln_err = "last_name must be a string"

    if type(first_name) is not str:
        raise TypeError(fn_err)
    if type(last_name) is not str:
        raise TypeError(ln_err)
    if last_name is "":
        print(f"My name is {first_name}")
    else:
        print(f"My name is {first_name} {last_name}")
