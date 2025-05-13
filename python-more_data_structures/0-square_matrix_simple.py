#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy = [list(fila) for fila in matrix]

    for filas in copy:
        for i, col in enumerate(filas):
            valor = filas[i]
            filas[i] = valor * valor
    return copy
