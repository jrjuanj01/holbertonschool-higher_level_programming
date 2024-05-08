#!/usr/bin/python3
for ltr in range(122, 96, -1):
    print("{}".format(chr(ltr) if ltr % 2 == 0 else chr(ltr - 32)), end="")
