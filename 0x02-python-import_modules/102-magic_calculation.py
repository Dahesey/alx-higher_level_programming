#!/usr/bin/python3


def magic_calculation(a, b):
    """match with holberton bytecode"""
    from calculator_ import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)
    else:
        return(sub(a, b))
