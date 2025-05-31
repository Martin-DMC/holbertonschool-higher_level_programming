#!/usr/bin/python3
"""
modulo que define la clase add_attribute(), la cual add
un nuevo atributo al objeto si eso es posible
"""


def add_attribute(clase, atrib, change):
    """
    esta funcion adiere atributos si eso es posible
    return:
        TypeError en caso de no ser posible
    """
    tipo = type(clase)
    tipos = (str, bool, float, tuple, type(None))

    if isinstance(clase, tipos):
        raise TypeError("can't add new attribute")
    else:
        if hasattr(tipo, '__slots__'):
            if atrib not in tipo.__slots__:
                if not hasattr(tipo, '__dict__'):
                    raise TypeError("can't add new atribute")
                else:
                    raise TypeError("can't add new attribute")
            else:
                setattr(clase, atrib, change)
        else:
            setattr(clase, atrib, change)
