#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    datos = argv
    cant = len(datos) - 1

    if cant != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    signo = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    
    if signo == "+":
        res = add(a, b)
        print("{:d} + {:d} = {:d}".format(a, b, res))
        exit(0)
    elif signo == '-':
        res = sub(a, b)
        print("{:d} - {:d} = {:d}".format(a, b, res))
        exit(0)
    elif signo == "*":
        res = mul(a, b)
        print("{:d} * {:d} = {:d}".format(a, b, res))
        exit(0)
    elif signo == "/":
        res = div(a, b)
        print("{:d} / {:d} = {:d}".format(a, b, res))
        exit(0)
    else:
        print(
            "Unknown operator. Available operators: +, -, * and /"
            )
        exit(1)
