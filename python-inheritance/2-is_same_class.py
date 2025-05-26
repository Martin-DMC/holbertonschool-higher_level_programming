#!/usr/bin/python3
"""
modulo que define una funcion para saber si eñ objeto
es exactamente una intancia de la clase especificada 
"""
def is_same_class(obj, a_class):
    """
    dicha funcion, devuelve True si es exactamente
    o False en cualquier otra instancia
    """
    return type(obj) == a_class