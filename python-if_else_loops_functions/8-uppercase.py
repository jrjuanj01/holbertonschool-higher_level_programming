#!/usr/bin/python3
def uppercase(str):
    for l in str:
        if ord('a') <= ord(l) <= ord('z'):
            L = chr(ord(l) - 32)
            print("{}".format(L), end="")
        else:
            print("{}".format(l), end="")
    print()
