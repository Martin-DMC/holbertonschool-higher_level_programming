#!/usr/bin/python3
"""
this module define a function that inserts a line of
text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    this function insert a new line if find matching in text with
    the string specified.
    args:
        filename: name of file to modificate
        search_string: string specified
        new_string: new string to insert
    """
    with open(filename, "r") as archivo:
        contenido = archivo.readlines()
    for i, line in enumerate(contenido):
        if search_string in line:
            contenido.insert(i + 1, new_string)
    with open(filename, "w") as archivo:
        archivo.writelines(contenido)
