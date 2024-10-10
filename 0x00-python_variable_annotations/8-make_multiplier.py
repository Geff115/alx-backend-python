#!/usr/bin/env python3
"""
This script uses a type-annotated function make_multiplier
that takes a float multiplier as arguments and returns a
function that multiplies a float by multiplier
"""

from typing import List, Dict, Tuple, Optional, Union
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    ARGS:
        - multiplier: A floating point number.

    RETURN:
        - a function that multiplies a float by
        multiplier
    """
    def multiply(x: float) -> float:
        return x * multiplier

    return multiply
