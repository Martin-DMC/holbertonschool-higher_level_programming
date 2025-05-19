#!/usr/bin/python3
"""text_identation es una funcion que toma como argumento un texto, lo
recorre y lo va dividiendo en frases.
luego imprime todas las frases cereadas con una <BLANKLINE> de espacio

arg:
    text = texto a dividir e imprimir
raise:
    text != str --> TypeError
"""


def text_indentation(text):
    """los caracteres de corte son '.' ':' '?'
    usa un while para crear la lista de lista y luego un for para imprimir
    cada una de las frases
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    cadena = ""
    lista = []
    while i < len(text):
        if text[i] == '?' or text[i] == '.' or text[i] == ':':
            cadena += text[i]
            cadena = list(cadena)
            lista.append(cadena)
            cadena = ""
            i += 1
        elif i == len(text) - 1:
            cadena += text[i]
            cadena = list(cadena)
            lista.append(cadena)
            cadena = ""
            i += 1
        else:
            cadena += text[i]
            i += 1
    for fila in lista:
        for i, letra in enumerate(fila):
            if letra == ' ' and i == 0:
                pass
            else:
                print(letra, end='')
        if not len(lista) == 1 or fila != lista[-1]:
            print("")
        if fila != lista[-1]:
            print("")
