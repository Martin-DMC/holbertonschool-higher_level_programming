#!/usr/bin/python3
"""
modulo que defina la clase Shape() como base
y las subclases Circle() y Rectangle()
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    clase Shape() declarada como clase base abstracta
    """
    @abstractmethod
    def area(self):
        """
        funcion que calcula el area de la forma
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        funcion que calcula el perimetro de la forma
        """
        pass


class Circle(Shape):
    """
    clase Circle() la cual hereda de la clase Shape()
    """
    def __init__(self, radius):
        """
        instanciacion de Circle
        """
        self.__radius = radius

    def area(self):
        """
        funcion que calcula el area de un circulo
        """
        area = math.pi * (self.__radius ** 2)
        return area

    def perimeter(self):
        """
        funcion que calcula el perimetro del circulo
        """
        perimetro = 2 * math.pi * abs(self.__radius)
        return perimetro


class Rectangle(Shape):
    """
    clase Rectangle() la cual hereda de la clase Shape()
    """
    def __init__(self, width, height):
        """
        instanciacion de Rectangle
        """
        self.__width = width
        self.__height = height

    def area(self):
        """
        funcion que calcula el area de un rectangulo
        """
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """
        funcion que calcula el perimetro de un rectangulo
        """
        perimetro = (self.__width + self.__height) * 2
        return perimetro


def shape_info(obj):
    """
    funcion que entrega la informacion del objeto instanciado
    """
    area = obj.area()
    perimetro = obj.perimeter()
    print(f"Area: {area}")
    print(f"Perimeter: {perimetro}")
