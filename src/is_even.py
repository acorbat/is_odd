def is_odd(x):
    """Returns True if x is odd

    Parameters
    ----------
    x: int
        integer to check if it is odd.

    Returns
    -------
    : bool
        Returns True if x is odd, else it returns False"""
    if not isinstance(x, int):
        raise TypeError('x must be an integer')

    if x % 2 == 1:
        return True
    else:
        return False


assert is_odd.__doc__ is not None

raised_typeerror = False
try:
    is_odd('das')
except TypeError:
    raised_typeerror = True

assert raised_typeerror

assert is_odd(2) is False

assert is_odd(1)