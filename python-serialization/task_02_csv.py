#!/usr/bin/python3
"""
this module define the function convert_cvs_to_json()
this function serialize a file.csv to file.json
"""
import csv
import json


def convert_csv_to_json(filename):
    """
    this function take a filename for open this file in
    a special mode for read the file.csv.
    after to copy the info in json type for make the file.json
    returns:
        True if successful
        and False in any other case
    """
    try:
        lista = []
        with open(filename, mode="r") as archivo_csv:
            contenido = csv.DictReader(archivo_csv)
            for fila in contenido:
                lista.append(fila)
        with open("data.json", "w") as archivo:
            json.dump(lista, archivo)
        return True
    except FileNotFoundError:
        return False
