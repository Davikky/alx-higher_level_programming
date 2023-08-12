#!/usr/bin/python3

from calculator_1 import add, sub, mul, div


def simple_calc(argv):
    """My simple calculator function


    Argument:
        argv: argument vector


    Returns:
        exit value. 1
    """

    num_arg = len(argv) - 1
    if num_arg != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    if operator == '+':
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, add(a, b)))
    elif operator == '-':
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, sub(a, b)))
    elif operator == '*':
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, mul(a, b)))
    elif operator == '/':
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")


if __name__ == "__main__":
    import sys
    simple_calc(sys.argv)
