#!/usr/bin/env python3
"""
This script uses a type-annotated function which takes
a list mxd_lst of integers and floats and returns their
sum as a float.
"""

from typing import List, Dict, Tuple, Optional, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    ARGS:
        - mxd_list: A list of integers and floats.

    RETURN:
        - The sum of the list as a float.
    """
    return float(sum(mxd_list))
