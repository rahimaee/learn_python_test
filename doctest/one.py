"""
>>> add(2,2)
4
>>> subtract(2,2)
0
>>> multiply(2,2)
4
"""


def add(x, y):
    """
    >>> add(2,2)
    4
    """
    return x + y


def subtract(x, y):
    """
    >>> subtract(2,2)
    0
    >>> subtract(4,2)
    2
    >>> subtract(2,4)
    -2
    """
    return x - y


def multiply(x, y):
    """
    >>> multiply(2,2)
    4
    >>> multiply(2,-1)
    -2
    """
    return x * y

# run test >> python -m doctest one.py
# see detail test >> python -m doctest -v one.py
