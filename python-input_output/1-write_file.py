#!/usr/bin/python3
"""
define la funcion write_file
la cual escribe en un archivo o lo crea si no existe
y retorna los caracteres escritos
"""


def write_file(filename="", text=""):
    """
    la funcion abre el archivo de una manera
    que si no existe lo crea.
    return:
        numero de caracteres escritos
    """
    with open(filename, "w") as archivo:
        charters = archivo.write(text)
        return charters
