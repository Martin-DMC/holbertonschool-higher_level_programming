#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if int(value):
            print("{:d}".format())
            return True

    except ValueError:
        return False
