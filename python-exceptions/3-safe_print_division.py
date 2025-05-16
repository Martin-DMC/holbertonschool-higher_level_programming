#!/usr/bin/python3
def safe_print_division(a, b):
    resultado = None
    try:
        if a is None or b is None:
            raise TypeError("Los argumentos no pueden ser None")
        resultado = a / b
    except ZeroDivisionError:
        return None
    except TypeError as e:
        resultado = None
    finally:
        if resultado is not None:
            print("Inside result: {:.2f}".format(resultado))
        else:
            print("Inside result: None")
        return resultado