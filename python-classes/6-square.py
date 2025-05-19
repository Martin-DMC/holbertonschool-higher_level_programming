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
    def __init__(self, size=0, position=(0, 0)):
        """documentacion de instancia
        arg:
            size (int, opcional): lado del cuadrado de esta instancia
            position(int, opcional): margen de izquierda y de arriba
        raises:
            size != int --> TypeError
            size < 0 --> ValueError
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or len(position) != 2 or \
                not all(isinstance(n, int) and n >= 0 for n in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(n, int) and n >= 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        position = self.__position

        if size == 0:
            print("")

        else:
            left = position[0]
            top = position[1]
            i = 0
            while i < top:
                print("")
                i += 1
            for i in range(size):
                print("_" * left + "#" * size)
