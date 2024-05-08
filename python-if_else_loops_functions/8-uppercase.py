#!/usr/bin/python3
def uppercase(str):
    for l in str:
        if ord('a') <= ord(l) <= ord('z'):
            l = chr(ord(l) - 32)
        print("{}".format(l), end="")
    print()
