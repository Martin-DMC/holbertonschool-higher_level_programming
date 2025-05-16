#!/usr/bin/python3
def safe_print_integer(value):
    try:
        numero = int(value)
        print("{:d}".format(numero))
        return True

    except ValueError:
        return False
