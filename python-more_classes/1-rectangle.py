#!/usr/bin/python3
"""
crea la clase Rectangle que esta vacia
"""


class Rectangle():
    """
    documentacion para la futura clase Rectangle()
    """
    def __init__(self, width=0, height=0):
        """
        documentacion de la instancia
        args:
            width: ancho
            height: largo
        Raises:
            width o height != int --> TypeError
            width o height < 0 --> ValueError
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    # -- GETTER --
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    # -- SETTER --
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
