#!/usr/bin/python3
from model_state import Base, State
import sys
import sqlalchemy


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Wrong usage")

    else:
        State(sys.argv[1], sys.argv[2], sys.argv[3])
