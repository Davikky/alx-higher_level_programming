#!/usr/bin/python3


def no_c(my_string):
    """Removes all characters c and C from a string"""

    output = my_string.translate({ord(i): None for i in 'cC'})
    return output
