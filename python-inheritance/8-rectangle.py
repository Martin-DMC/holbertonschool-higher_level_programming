#!/usr/bin/python3
"""
modulo que crea la subclase Rectangle() que hereda de
BaseGeometry()
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    clase rectangulo la cual valida los valores entregados
    deben ser enteros y positivos
    """
    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
