#!/usr/bin/python3
"""
this module define a script,
this function of the scrip is adds all arguments to a
Python list, and then save them to a file.
"""


import json
import sys
save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file


try:
    lista = load_json("add_item.json")
    datos = sys.argv

    for i, dato in enumerate(datos):
        if i == 0:
            pass
        else:
            lista.append(dato)
    save_to_json(lista, "add_item.json")
except FileNotFoundError:
    lista = []
    datos = sys.argv

    for i, dato in enumerate(datos):
        if i == 0:
            pass
        else:
            lista.append(dato)
    save_to_json(lista, "add_item.json")
