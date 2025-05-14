#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    lista = []
    for key in a_dictionary:
        lista.append(key)
    lista = sorted(lista)

    for key in lista:
        for clave, valor in a_dictionary.items():
            if clave == key:
                print(f"{clave}: {valor}")
