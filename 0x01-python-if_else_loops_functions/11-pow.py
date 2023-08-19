#!/usr/bin/python3


def pow(a, b):
    res = 1
    base = 1
    numb = 0

    if b < 0:
        numb = b
        b *= -1

    for i in range(b):
        res *= a

    if numb < 0:
        result = base / res
    elif numb == 1:
        result = 1
    else:
        result = res

    return result
