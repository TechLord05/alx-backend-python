#!/usr/bin/env python3

"""Module that contains  a type-annotated function make_multiplier
that takes a float multiplier as argument and returns a function
that multiplies a float by multiplier.
"""

import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """Function that takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier.
    """
    def multiply(n: float) -> float:
        """Function that multiplies a float by multiplier.
        """
        return n * multiplier
    return multiply
