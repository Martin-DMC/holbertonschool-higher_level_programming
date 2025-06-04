#!/usr/bin/python3
"""
this module is a basic serialization and define two function.
the first function serialize a python dictonary to json file
the last function deserialize the json file to py dict
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    this function make or rewrite and save a json file
    args:
        data = to save
        filename = future name of the file
    """
    with open(filename, "w") as archivo:
        json.dump(data, archivo)


def load_and_deserialize(filename):
    """
    this function loading and deserialize json files and
    returns the python dict
    """
    with open(filename, "r") as archivo:
        return json.load(archivo)
