#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    existe = 0
    for clave in a_dictionary:
        if clave == key:
            existe = 1
    if existe == 1:
        del a_dictionary[key]
        return a_dictionary
    else:
        return a_dictionary
