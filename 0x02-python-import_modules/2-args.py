#!/usr/bin/python3

import sys

if __name__ == "__main__":
    n_args = len(sys.argv) - 1
    args = sys.argv[1:]

    print("{} argument{}".format(n_args, 's' if n_args != 1 else ''), end="")
    if n_args == 0:
        print(".")
    else:
        print(":")
        for i, arg in enumerate(args):
            print("{}: {}".format(i + 1, arg))
