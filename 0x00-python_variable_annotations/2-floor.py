#!/usr/bin/env python3
"""
This script uses a type-annotated function floor which
takes a float n as argument and
returns the floor of the float.
"""

from typing import List, Dict, Tuple, Optional, Union
import math


def floor(n: float) -> int:
    """
    ARGS:
        - n: A floating point number.

    RETURN:
        - floor of n.
    """
    return math.floor(n)
