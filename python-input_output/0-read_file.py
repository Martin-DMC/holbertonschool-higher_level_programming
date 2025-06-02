#!/usr/bin/python3
"""
define la funcion read_file(filename=""):
    la cual lee un archivo de texto (utf8)
    e imprime en la salida estandar
"""


def read_file(filename=""):
    """
    esta funcion abre el archivo y despues imprime
    el contenido por pantalla
    """
    with open(filename, "r") as archivo:
        print(archivo.read(), end="")
