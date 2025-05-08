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
    
    match signo:
        case "+":
            res = add(a, b)
            print("{:d} + {:d} = {:d}".format(a, b, res))
            exit(0)
        case "-":
            res = sub(a, b)
            print("{:d} - {:d} = {:d}".format(a, b, res))
            exit(0)
        case "*":
            res = mul(a, b)
            print("{:d} * {:d} = {:d}".format(a, b, res))
            exit(0)
        case "/":
            res = float(div(a, b))
            print("{:d} / {:d} = {:.2f}".format(a, b, res))
            exit(0)
        case _:
            print(
                "Unknown operator. Available operators: +, -, * and /"
                )
            exit(1)