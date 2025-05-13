#!/usr/bin/python3
def multiple_returns(sentence):
    largo = len(sentence)
    if largo == 0:
        first = None
    else:
        first = sentence[0]

    return largo, first
