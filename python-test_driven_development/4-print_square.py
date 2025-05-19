#!/usr/bin/python3
"""
la funcion print_square imprime por pantalla un "cuadrado"
de la medida que le pasamos.

arg:
    size = tamaño del cuadrado
raises:
    size < 0 --> ValueError
    size != int, size < 0.0 --> TypeError
"""


def print_square(size):
    """si el argumento logra pasar por los filtros
    la funcion imprime el cuadrado indicado, sino
    devuelve un error"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif isinstance(size, float):
        if size < 0:
            raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    i = 0
    while i < size:
        print("#" * size)
        i += 1
