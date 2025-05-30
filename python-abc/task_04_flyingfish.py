#!/usr/bin/python3
"""
define la clase FlyingFish() la cual hereda de
dos clases padre, Bird() y Fish()
"""


class Fish():
    """
    clase Fish(), contiene dos metodos.
    habitat(), swim().
    retornan un print
    """
    def swim(self):
        """
        Return:
            print lo que esta haciendo
        """
        return print("The fish is swimming")

    def habitat(self):
        """
        Return:
            print cual es el habitat
        """
        return print("The fish lives in water")


class Bird():
    """
    clase Bird(), contiene dos metodos.
    habitat(), fly().
    retornan un print
    """
    def fly(self):
        """
        Return:
            print lo que esta haciendo
        """
        return print("The bird is flying")

    def habitat(self):
        """
        Return:
            print cual es el habitat
        """
        return print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    clase FlyingFish(), hereda de dos clases
    Fish() y Bird()
    retorna un print
    """
    def fly(self):
        """
        Return:
            print lo que esta haciendo
        """
        return print("The flying fish is soaring!")

    def swim(self):
        """
        Return:
            print lo que esta haciendo
        """
        return print("The flying fish is swimming!")

    def habitat(self):
        """
        Return:
            print cual es el habitat
        """
        return print("The flying fish lives both in water and the sky!")
