#!/usr/bin/env python3

"""Module that contains a type-annotated function
to_kv that takes a string k and an int OR
float v as arguments and returns a tuple.
"""

import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """Function that takes a string k and an int OR float v as arguments
    and returns a tuple.
    """
    return (k, v ** 2)
