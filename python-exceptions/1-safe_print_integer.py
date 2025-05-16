#!/usr/bin/python3
def safe_print_integer(value):
    try:
        int(value)
        print("{:d}".format())

    except ValueError:
        return False

    return True
