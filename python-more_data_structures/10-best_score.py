#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        first_element = next(iter(a_dictionary.items()))
        key = first_element[0]
        value = first_element[1]
        for clave, valor in a_dictionary.items():
            if int(valor) > value:
                key = clave
        return key
