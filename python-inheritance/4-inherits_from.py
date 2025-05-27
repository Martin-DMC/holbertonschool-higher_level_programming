#!/usr/bin/python3
"""
modulo que define una funcion de verificacion
"""


def inherits_from(obj, a_class):
    """
    la funcion devuelve True si el objeto es una clase que
    heredo (directa o indirectamente) de la clase especificada
    sino devuelve False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
