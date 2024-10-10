#!/usr/bin/env python3
"""
This script uses a type-annotated function concat that
takes a string str1 and a string str2 as arguments and
returns a concatenated string.
"""

from typing import List, Dict, Tuple, Optional, Union


def concat(str1: str, str2: str) -> str:
    """
    ARGS:
        - str1: A string
        - str2: A string

    RETURN:
        - A concatenated string, i.e str1 + str2
    """
    return str1 + str2
