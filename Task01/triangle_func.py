import doctest


class IncorrectTriangleSides(Exception):
    pass


def get_triangle_type(first_side: int, second_side: int, third_side: int) -> str:
    """
    Function for checking type of triangle
    :param first_side: first side of triangle (int)
    :param second_side: second side of triangle (int)
    :param third_side: third side of triangle (int)
    :return: type of triangle (str)
    :raises: IncorrectTriangleSides: if sides was set incorrectly

    >>> get_triangle_type(7, 7, 7)
    'equilateral'
    >>> get_triangle_type(7, 9, 11)
    'nonequilateral'
    >>> get_triangle_type(7, 7, 17)
    'isosceles'
    >>> get_triangle_type("a","b","c")
    Traceback (most recent call last):
     ...
    IncorrectTriangleSides: Sides set incorrectly
    >>> get_triangle_type(1, 2, 3)
    Traceback (most recent call last):
     ...
    IncorrectTriangleSides: Sides set incorrectly
    """

    if (first_side + second_side <= third_side
            or first_side + third_side <= second_side
            or second_side + third_side <= first_side):
        raise IncorrectTriangleSides('Sides set incorrectly')

    if first_side != second_side != third_side:
        return "nonequilateral"
    elif first_side == second_side == third_side:
        return "equilateral"
    else:
        return "isosceles"


if __name__ == '__main__':
    doctest.testmod()
