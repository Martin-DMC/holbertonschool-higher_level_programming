#!/usr/bin/python3
def crear_tuple(tuple_=()):
    if len(tuple_) == 0:
        tuple_ = (0, 0)
        return tuple_
    elif len(tuple_) == 1:
        tuple_ = (tuple_[0], 0)
        return tuple_
    elif len(tuple_) >= 2:
        tuple_ = (tuple_[0], tuple_[1])
        return tuple_


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = list(crear_tuple(tuple_a))
    tuple_b = list(crear_tuple(tuple_b))
    valor_1 = (tuple_a[0] + tuple_b[0])
    valor_2 = (tuple_a[1] + tuple_b[1])
    new_tuple = (valor_1, valor_2)
    return new_tuple
