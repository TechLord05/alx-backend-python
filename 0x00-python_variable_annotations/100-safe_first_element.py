#!/usr/bin/env python3

"""Module that annotates the below function's parameters
    and return values with the appropriate types

-   def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
"""

from typing import List, Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Function that takes a list lst as argument
    and returns its first element if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
