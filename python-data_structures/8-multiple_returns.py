#!/usr/bin/python3
def multiple_returns(sentence):
    char = sentence[:1] if len(sentence) > 0 else None
    t = (len(sentence), char)
    return t
