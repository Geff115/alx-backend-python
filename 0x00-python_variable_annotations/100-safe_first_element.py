#!/usr/bin/env python3
"""
This script Augment the following code with the correct duck-typed annotations:

N.B: The types of the elements of the input are not known
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    ARGS:
        - lst: A sequence containing elements of any type

    RETURN:
        - Either an element of any type or None
    """
    if lst:
        return lst[0]
    else:
        return None
