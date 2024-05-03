#!/usr/bin/env python3

""" Module that contains a type-annotated function (sum_mixed_list)
that takes a list (mxd_list) of integers and floats as arguments and
returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Function to return the sum of a list of integers and floats.
    """
    mxd_sum = 0.0

    for num in mxd_list:
        if isinstance(num, int) or isinstance(num, float):
            mxd_sum += num

    return mxd_sum
