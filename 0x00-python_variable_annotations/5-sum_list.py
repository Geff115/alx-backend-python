#!/usr/bin/env python3
"""
This script uses a type-annotated function sum_list which
takes a list input_list of floats as argument and returns
their sum.
"""

from typing import List, Dict, Tuple, Optional, Union


def sum_list(input_list: List[float]) -> float:
    """
    ARGS:
        - input_list: A list of floating point numbers.

    RETURN:
        - sum of all the floats in the list.
    """
    return sum(input_list)
