#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    if a == 0:
        b = None
    else:
        b = sentence[:1]
    t = (a, b)
    return t
 