#!/usr/bin/python3
"""
this module define the function pascal_triangle().
this triangle is follow something rules.
all list beggin with 1 and also finish with 1
the center numbers go make with the result of add value of that
position in the beffore list and the position value beffore
"""


def pascal_triangle(n):
    """
    this funtion receive one parameter and
    make to the triangle folowing the rules of
    triangle pascual.
    if parameter is a int <= 0 the function
    return a empty list
    else the function return the triangle
    """
    i = 0
    triangle = []
    if n <= 0:
        return triangle
    while i < n:
        j = 0
        lista = []
        while j <= i:
            if j == 0:
                num = 1
                lista.append(num)
            elif j == i:
                num = 1
                lista.append(num)
            else:
                num = triangle[i - 1][j] + triangle[i - 1][j - 1]
                lista.append(num)
            j += 1
        triangle.append(lista)
        i += 1
    return triangle
