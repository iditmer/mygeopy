import math, numbers

def hypot(a: float, b: float) -> float:
    """
    Calculate the hypotenuse of a right triangle.

    >>> hypot(3,4)
    5.0
    """

    if not isinstance(a, numbers.Real) or not isinstance(b, numbers.Real):
        raise TypeError('Side lengths must be real-valued numbers.')
    if a < 0 or b < 0:
        raise ValueError('Side lenghts must be positive values.')

    return math.sqrt(a * a + b * b)

if __name__ == "__main__":
    import doctest
    doctest.testmod()