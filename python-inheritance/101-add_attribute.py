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
    tipos = (int, str, bool, float, tuple, type(None))

    if isinstance(clase, tipos):
        raise TypeError("can't add new attribute")
    else:
        slot = hasattr(tipo, '__slots__')
        _dict = hasattr(tipo, '__dict__')
        if slot is True and _dict is False:
            if atrib in tipo.__slots__:
                setattr(clase, atrib, change)
            else:
                raise TypeError("can't add new attribute")
        else:
            setattr(clase, atrib, change)
