#!/usr/bin/python3
"""Returns:
        el resultado de la suma entera.

    Raises:
        TypeError: si a no es entero o flotante
        TypeError: si b no es entero o flotante
"""
def add_integer(a, b=98):
    """Args:
        a: 1er numero.
        b: 2do numero. por default 98.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    try:
        int_a = int(a)
    except OverflowError:
        raise TypeError("a cannot be converted to an integer (overflow)")
    except ValueError:
        raise TypeError("a must be an integer or float (not NaN)")

    try:
        int_b = int(b)
    except OverflowError:
        raise TypeError("b cannot be converted to an integer (overflow)")
    except ValueError:
        raise TypeError("b must be an integer or float (not NaN)")

    return int_a + int_b
