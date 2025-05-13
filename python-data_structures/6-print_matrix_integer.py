#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for filas in matrix:
        for i, colum in enumerate(filas):
            print("{:d}".format(int(colum)), end="")
            if i < len(filas) - 1:
                print(" ", end="")
        print("")
