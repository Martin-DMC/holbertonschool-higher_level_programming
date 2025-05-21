#!/usr/bin/python3
"""
creacion de la clase Rectangle()
"""


class Rectangle():
    """
    documentacion para la clase Rectangle()
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

    def area(self):
        """
        calcula el area del rectangulo.
        return:
            resultado de la operacion o 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * self.__height

    def perimeter(self):
        """
        calcula el perimetro del rectangulo.
        return:
            resultado de la operacion
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        representa el rect
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            rectangulo = ""
            for i in range(self.__height):
                rectangulo += "#" * self.__width
                if i < self.height - 1:
                    rectangulo += "\n"
            return rectangulo

    def __repr__(self):
        nombre = type(self).__module__ + "." + type(self).__name__
        address = hex(id(self))
        return f"<{nombre} object at {address}"
