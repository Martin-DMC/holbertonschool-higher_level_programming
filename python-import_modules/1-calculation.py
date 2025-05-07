#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    res = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, res))
    res = sub(a, b)
    print("{:d} - {:d} = {:d}".format(a, b, res))
    res = mul(a, b)
    print("{:d} * {:d} = {:d}".format(a, b, res))
    res = div(a, b)
    print("{:d} / {:d} = {:d}".format(a, b, res))
