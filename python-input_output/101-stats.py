#!/usr/bin/python3
"""
this module define a script that reads stdin
line by line and computes metrics how the size of file
and the count of HTTP status code.
also define a function that print all data
"""
import sys


def print_data(dictionary):
    """
    simple function that print all keys and values from
    this dictionary.
    in ascending order and only print values > 0 in a special format
    """
    lista = dictionary.keys()
    lista = sorted(lista)
    for i in lista:
        if dictionary[i] > 0:
            print(f"{i}: {dictionary[i]}")


def main():
    entrada = sys.stdin
    tamaño_archivo = 0
    cont_status = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    cont_lineas = 0
    try:
        for line in entrada:
            lista = list(line.split(' '))
            status = lista[-2]
            size = lista[-1]
            try:
                status = int(status)
                size = int(size)
            except ValueError:
                continue
            tamaño_archivo += size
            if status in cont_status.keys():
                cont_status[status] += 1
            cont_lineas += 1
            if (cont_lineas % 10) == 0:
                cont_lineas = 0
                print(f"File size: {tamaño_archivo}")
                print_data(cont_status)
                for key in cont_status.keys():
                    cont_status[key] = 0
        print(f"File size: {tamaño_archivo}")
        print_data(cont_status)
    except KeyboardInterrupt:
        print(f"File size: {tamaño_archivo}")
        print_data(cont_status)


if __name__ == '__main__':
    main()
