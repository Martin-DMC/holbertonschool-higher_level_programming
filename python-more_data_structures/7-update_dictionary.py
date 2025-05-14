#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_element = 0
    for clave in a_dictionary:
        if clave == key:
            new_element = 1
    if new_element == 1:
        for clave, valor in a_dictionary.items():
            if clave == key:
                a_dictionary[clave] = value
    else:
        a_dictionary[key] = value

    return a_dictionary
