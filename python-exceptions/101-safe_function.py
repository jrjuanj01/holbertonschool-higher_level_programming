#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        return fct(*args)
    except (ValueError, ZeroDivisionError, IndexError, TypeError) as err:
        print("Exception:", err, file=stderr)
        return None
