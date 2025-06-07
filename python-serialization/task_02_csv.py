#!/usr/bin/python3
"""
"""
import csv
import json


def convert_csv_to_json(filename):
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
