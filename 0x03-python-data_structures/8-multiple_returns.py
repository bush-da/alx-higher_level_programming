#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
        ret = [len(sentence), None]
    else:
        ret = [len(sentence), sentence[0]]

    return tuple(ret)
