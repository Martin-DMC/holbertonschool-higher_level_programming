#!/usr/bin/python3
"""
modulo que define la clase Mylist.
"""


class MyList(list):
    """
    clase Mylist, la cual va a tener 1 metodo
    print_sorted
    """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        lista = sorted(self)
        print(lista)
