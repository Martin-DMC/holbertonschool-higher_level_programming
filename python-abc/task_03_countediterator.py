#!/usr/bin/python3
"""
define la funcion CountedIterator() la cual modifica iter
"""


class CountedIterator():
    """
    clase CountedIterator() es una extencion modificada de la funcion iter(),
    esta clase lleva la cuenta de los elementos iterados
    """
    def __init__(self, some_iterable):
        """
        instanciacion de la clase
        """
        self.iterator = iter(some_iterable)
        self.count = 0

    def __iter__(self):
        """
        Devuelve la instancia del iterador para permitir la iteración
        """
        return self

    def __next__(self):
        """
        toma el siguiente elemento en la fila y suma 1 al contado y
        retorna el elemento
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise

    def get_count(self):
        """
        devuelve el contador de elementos iterados
        """
        return self.count
