def is_even(x):
    """Returns True if x is even

    Parameters
    ----------
    x: int
        integer to check if it is even.

    Returns
    -------
    : bool
        Returns True if x is even, else it returns False"""
    if not isinstance(x, int):
        raise TypeError('x must be an integer')

    if x % 2 == 0:
        return True
    else:
        return False


assert is_even.__doc__ is not None

raised_typeerror = False
try:
    is_even('das')
except TypeError:
    raised_typeerror = True

assert raised_typeerror

assert is_even(2)

assert is_even(1) is False