#!/usr/bin/env python3
"""
This script simply just annotates this function:

def element_length(lst):
    return [(i, len(i)) for i in lst]
"""

from typing import List, Dict, Tuple, Optional, Union
from typing import Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    ARGS:
        - lst: A list of strings or elements with a length
        attribute.

    RETURN:
        - A list of tuples, where each tuple contains an element
        from the input list and its length.
    """
    return [(i, len(i)) for i in lst]
