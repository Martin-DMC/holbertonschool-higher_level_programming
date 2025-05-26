#!/usr/bin/python3
"""
modulo para funcion que define si es una instancia de
o si el objeto es una instancia de, una clase que
heredo de; La clase espesificada"""


def is_kind_of_class(obj, a_class):
    """
    la funcion recibe un objeto y una clase y retorna
    True si es verdad
    """
    return isinstance(obj, a_class)
