#!/usr/bin/python3
"""
this modulo define una funcion que escribe un objeto
en un archivo de texto, usando una representacion JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """
    la funcion abre el futuro archivo JSON para luego
    escribir el objeto en dicho archivo.JSON
    Return:
        el objeto en representacion JSON
    """
    with open(filename, "w") as archivo:
        return json.dump(my_obj, archivo)
