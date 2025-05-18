#!/usr/bin/python3

matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

# Casos borde adicionales
print("\nCaso 2: Matriz con floats")
matrix_floats = [
    [1.5, 2.5, 3.5],
    [4.5, 5.5, 6.5]
]
print(matrix_divided(matrix_floats, 2))

print("\nCaso 3: Matriz con un solo elemento")
matrix_un_elemento = [[10]]
print(matrix_divided(matrix_un_elemento, 5))

print("\nCaso 4: Matriz vacía")
matrix_vacia = []
try:
    print(matrix_divided(matrix_vacia, 2))  # Esto debería lanzar un TypeError
except Exception as e:
    print(f"Excepción capturada: {e}")

print("\nCaso 5: Matriz con filas de diferente tamaño")
matrix_filas_diferentes = [
    [1, 2, 3],
    [4, 0]
]
try:
    print(matrix_divided(matrix_filas_diferentes, 1))  # Esto debería lanzar un TypeError
except Exception as e:
    print(f"Excepción capturada: {e}")

print("\nCaso 6: Divisor como float")
divisor_float = 2.5
print(matrix_divided(matrix, divisor_float))

print("\nCaso 7: Matriz con un elemento que no es ni int ni float")
matrix_tipo_incorrecto = [
    [1, 2, "a"],
    [4, 5, 6]
]
try:
    print(matrix_divided(matrix_tipo_incorrecto, 2))  # Esto debería lanzar un TypeError
except Exception as e:
    print(f"Excepción capturada: {e}")

print("\nCaso 8: Matriz con valores muy grandes")
matrix_valores_grandes = [
    [10**10, 2 * 10**10, 3 * 10**10],
    [4 * 10**10, 5 * 10**10, 6 * 10**10]
]
print(matrix_divided(matrix_valores_grandes, 10**9))

print("\nCaso 9: Matriz con valores negativos")
matrix_negativos = [
    [-1, 2, 0],
    [-4, 0, 0]
]
print(matrix_divided(matrix_negativos, 'a'))
