#!/usr/bin/python3
"""
this module define the function load_from_json()
this function create an objects fron JSON file
"""
import json


def load_from_json_file(filename):
    """
    this function open the json file in read mode for
    after go print this information of the file
    Return:
        the data contain of the file
    """
    with open(filename, "r") as archivo:
        datos = json.load(archivo)
        return datos
