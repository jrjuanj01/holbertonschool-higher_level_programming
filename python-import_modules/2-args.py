#!/usr/bin/python3
import sys
argc = len(sys.argv)
idx = 0
if __name__ == "__main__":
    if argc == 1:
        print("0 arguments.")
    elif argc == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    elif argc > 2:
        print("{} arguments:".format(argc - 1))
        for args in sys.argv[1:]:
            idx += 1
            print("{}: {}".format((idx), args))
