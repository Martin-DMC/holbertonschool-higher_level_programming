#!/usr/bin/python3
"""
modulo que crea la clase BaseGeometry() y la subclase Rectangle()
"""


class BaseGeometry():
    """
    clase BaseGeometry()
    valida los enteros y tiene una 'futura' funcion que calcula
    el area
    """
    def integer_validator(self, name, value):
        """
        funcion para validar los atributos entregados
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def area(self):
        """
        funcion 'que va' a calcular el area del objeto
        """
        raise Exception("area() is not implemented")

class Rectangle(BaseGeometry):
    """
    clase rectangulo la cual valida los valores entregados
    deben ser enteros y positivos
    """
    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
