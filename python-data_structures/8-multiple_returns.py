#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        a = 0 
        b = None
    else:
        a = len(sentence)
        b = sentence[:1]
    t = (a, b)
    return t
