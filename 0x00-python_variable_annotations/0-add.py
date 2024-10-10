#!/usr/bin/python3
"""
This script uses a type-annotated function add
that takes a float a and a float b as arguments
and returns their sum as a float.
"""


from typing import List, Dict, Tuple, Optional, Union


def add(a: float, b: float) -> float:
    """
    ARGS:
        - a: A floating point number.
        - b: A floating point number.

    RETURN:
        - (a + b) -> float.
    """
    return a + b
