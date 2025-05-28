#!/usr/bin/python3
"""
contiene la clase Animal()
y las subclases Perro() y Gato()
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    clase base Animal() la cual va a tener 2 derivadas
    """
    @abstractmethod
    def sound(self):
        """
        metodo abstracto que imitara el sonido de los animales
        """
        pass


class Dog(Animal):
    """
    subclase Dog() de la clase Animal()
    """
    def sound(self):
        """
        funcion que implementa el metodo abstracto de la clase animal
        """
        return "Bark"


class Cat(Animal):
    """
    subclase Cat() de la clase Animal()
    """
    def sound(self):
        """
        funcion que implementa el metodo abstracto de la clase animal
        """
        return "Meow"
