#!/usr/bin/python3
"""
este modulo define la funcion from_json_string()
la cual devuelve un objeto representado pot una
cadena json
"""
import json


def from_json_string(my_str):
    """
    la funcion maneja una representacion json y la
    convierte en un objeto de python para devolver
    el resultado
    """
    datos_json = json.loads(my_str)
    return datos_json
