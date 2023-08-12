#!/usr/bin/python3

import hidden_4


def uncover():
    """My function to uncover hidden_4 module


    Args:
        N/A


    Returns:
        No return value.
    """

    name = dir(hidden_4)
    for i in name:
        if i[:2] != '__':
            print("{:s}".format(i))


if __name__ == "__main__":
    uncover()
