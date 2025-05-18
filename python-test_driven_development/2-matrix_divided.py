#!/usr/bin/python3
"""
   matrix != enteros o flotantes: except TypeError 
   'matrix must be a matrix (list of lists) of integers/floats'

   listas != tamaño: except TypeError 
   'Each row of the matrix must have the same size'

   div != int o float: except TypeError 'div must be a number'

   div 0: except ZeroDivicionError 'division by zero'

   retorna nueva matrix
"""


def matrix_divided(matrix, div):
    """
    divide los elementos de las filas con div
    si pasa las excepciones
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix:
        igual = 0
        largo = len(matrix[0])
        for fila in matrix:
            if len(fila) == largo:
                igual = 0
            else:
                igual += 1
        if igual != 0:
            raise TypeError("Each row of the matrix must have the same size")
    for fila in matrix:
        for num in fila:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix \
                    (list of lists) of integers/floats")

    nueva_matriz = []
    for fila in matrix:
        nueva_fila = [round(elemento / div, 2) for elemento in fila]
        nueva_matriz.append(nueva_fila)
    return nueva_matriz
