#!/usr/bin/python3
"""
define la clase VerboseList(), la cual hereda de list
"""


class VerboseList(list):
    """
    clase VerboseList(), la cual retorna un mensaje cada ves
    que usamos los metodos de list
    """
    def append(self, item):
        """
        funcion de list que agrega un alemento
        """
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, item):
        """
        funcion de list que extiene la lista
        """
        super().extend(item)
        x = len(item)
        print(f"Extended the list with {x} items.")

    def remove(self, item):
        """
        funcion de list que elimina un valor
        """
        try:
            print(f"Removed {item} from the list.")
            super().remove(item)
        except ValueError:
            raise ValueError("valor inexistente")

    def pop(self, index=None):
        """
        funcion de list que elimina el valor de dicho index
        o elimina el ultimo elemento si el index el none
        """
        try:
            if index is not None:
                item = self[index]
                print(f"Popped {item} from the list.")
                super().pop(index)
            else:
                item = self[-1]
                print(f"Popped {item} from the list.")
                super().pop()
        except IndexError:
            print("error de indice")
