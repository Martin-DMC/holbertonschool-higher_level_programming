#!/usr/bin/python3
"""
modulo que crea la subclase Square() que hereda de
Rectangle()
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    subclase Scuare() la cual hereda de Rectangle
    """
    def __init__(self, size):
        self.__size = self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
        funcion para calcular el area del cuadrado
        """
        return super().area()

    def __str__(self):
        """
        funcion que devuelve una cadena de string para print
        """
        return f"[Square] {self.__size}/{self.__size}"
