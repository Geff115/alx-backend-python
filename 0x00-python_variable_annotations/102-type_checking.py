#!/usr/bin/env python3
"""
This script fixes a code base that has a
type checking error.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    ARGS:
        - lst: A tuple of integers, where ... means the tuple can
        be of any length.
        - factor: An integer.

    RETURN: A List[int] instead of a tuple to match the list
    comprehension.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


# Convert the list to a tuple
array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Change 3.0 to 3 (an integer)
