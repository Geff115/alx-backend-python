#!/usr/bin/env python3
"""
This script uses a type-annotated function to_str
that takes a float n as argument and returns a string
representation of the float
"""

from typing import List, Dict, Tuple, Optional, Union


def to_str(n: float) -> str:
    """
    ARGS:
        - n: a floating point number.

    RETURN:
        - string rep of the float.
    """
    return str(n)
