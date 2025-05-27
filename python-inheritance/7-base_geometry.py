#!/usr/bin/python3
"""
modulo que cre la clase BaseGeometry()
"""


class BaseGeometry():
    """
    clase BaseGeometry
    en este caso esta vacia
    """
    def integer_validator(self, name, value):
        """
        funcion para validar los atributos entregados
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def area(self):
        """
        funcion que va a calcular el area del objeto
        """
        raise Exception("area() is not implemented")
