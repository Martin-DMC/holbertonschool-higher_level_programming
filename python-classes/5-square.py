#!/usr/bin/python3
"""
descripcion del modulo
crea una clase Square() vacia
"""


class Square():
    """
    aca va la documentacion de la clase Square
    crea la clase Square() vacia
    """
    def __init__(self, size=0):
        """documentacion de instancia
        arg:
            size (int, opcional): lado del cuadrado de esta instancia
        raises:
            size != int --> TypeError
            size < 0 --> ValueError
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calcula y retorna el área del cuadrado.

        Return:
            int: El área del cuadrado.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        imprime el cuadrado 'visual'
        Return:
            el cuadrado por pantalla
        """
        size = self.__size
        if size == 0:
            print("")
        else:
            for i in range(size):
                print("#" * size)
