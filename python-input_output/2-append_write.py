#!/usr/bin/python3
"""
se define la funcion append_write(), la cual agrega
la cadena indicada al final del contenido.
"""


def append_write(filename="", text=""):
    """
    la funcion agrega la cadena text al final del contenido
    de filename, si filename no existe lo crea.
    return:
        cantidad de caracteres escrito
    """
    with open(filename, "a") as archivo:
        cantidad = archivo.write(text)
        return cantidad
