#!/usr/bin/python3
"""
define la funcion to_json_string(), la cual devuelve la
reprecentacion json de un objeto
"""
import json


def to_json_string(my_obj):
    """
    devuelve la repreentacion json de un objeto
    de python
    return:
        una cadena de texto
    """
    return json.dumps(my_obj)
