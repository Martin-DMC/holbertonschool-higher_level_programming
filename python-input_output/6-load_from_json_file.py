#!/usr/bin/python3
"""
this module define the function load_from_json()
this function create an objects fron JSON
"""
import json


def load_from_json_file(filename):
    """
    """
    with open(filename, "r") as archivo:
        datos = json.load(archivo)
        return datos
