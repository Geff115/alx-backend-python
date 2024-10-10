#!/usr/bin/env python3
"""
This script uses a type-annotated function to_kv that takes
a string k and an int OR float v as arguments and returns
a tuple.
"""

from typing import List, Dict, Tuple, Optional, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    ARGS:
        - k: a string
        - v: an integer or a float

    RETURN:
        - a tuple which contains the two elements
        i.e. the string, and the square of the int/float
        number.
    """
    return (k, pow(v, 2))
