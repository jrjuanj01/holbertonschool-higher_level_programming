#!/usr/bin/python3ch
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if __name__ == "__main__":
        if a < b: 
            c = add(a, b)
            for i in range(4, 6):
                c = c + i
            return c
        else:
            return sub(a, b)