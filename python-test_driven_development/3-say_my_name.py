#!/usr/bin/python3
"""
la funcion say_my_name imprime el nombre y apellido que recibe

args:
    first_name = nombre
    last_name = apellido

raises:
    si uno de los dos nombres no es un texto
    devuelve un mensaje

return:
    la imprecion de nombre y apellido entregado
"""


def say_my_name(first_name, last_name=""):
    """
    la funcion verifica los datos entregados y decide
    si no son texto devuelve raises
    si son textos sigue con su funcionamiento
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    return print(f"My name is {first_name} {last_name}")
