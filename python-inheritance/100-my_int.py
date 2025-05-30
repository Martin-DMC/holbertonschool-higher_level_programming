#!/usr/bin/python3
"""
define la clase MyInt() que ereda de int()
"""


class MyInt(int):
    """
    la clase MyInt(), es una modificacion de int()
    la cual invierte el return de los comparadores logicos
    """
    def __eq__(self, x):
        return super().__ne__(x)

    def __ne__(self, x):
        return super().__eq__(x)

    def __lt__(self, x):
        return super().__gt__(x)

    def __gt__(self, x):
        return super().__lt__(x)
