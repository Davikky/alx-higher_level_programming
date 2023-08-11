#!/usr/bin/python3

if __name__ == "__main__":

    a = 10

    b = 5

    import calculator_1 as cal

    result_add = cal.add(a, b)
    result_sub = cal.sub(a, b)
    result_mul = cal.mul(a, b)
    result_div = cal.div(a, b)

    print("{} + {} = {}".format(a, b, result_add))
    print("{} - {} = {}".format(a, b, result_sub))
    print("{} * {} = {}".format(a, b, result_mul))
    print("{} / {} = {}".format(a, b, result_div))
    
