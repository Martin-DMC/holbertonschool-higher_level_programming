#!/usr/bin/python3
"""
define las clases SwimMixin() y FlyMixin()
para abordar el tema de mixin en python
"""


class SwimMixin():
    """
    clase SwimMixim().
    contiene el metodo swim()
    retorna un print
    """
    def swim(self):
        """
        return:
            que esta haciendo
        """
        return print("The creature swims!")


class FlyMixin():
    """
    clase FlyMixim().
    contiene el metodo fly()
    retorna un print
    """
    def fly(self):
        """
        return:
            que esta haciendo
        """
        return print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    clase Dragon(), hereda de las clases mixin.
    hereda el metodo swim(), fly() y ademas contiene
    el metodo roar()
    retorna un print
    """
    def roar(self):
        """
        return:
            lo que esta haciendo
        """
        return print("The dragon roars!")
