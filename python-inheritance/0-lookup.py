#!/usr/bin/python3
"""
modulo que define una funcion que devuelve una lista de lo
que contiene el objeto a examinar
"""


def lookup(obj):
    """
    funcion que devuelve la lista dicha
    """
    return dir(obj)
