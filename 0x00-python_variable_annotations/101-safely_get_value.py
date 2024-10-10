#!/usr/bin/env python3
"""
This script add type annotations to the function

Hint: look into TypeVar

def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
"""

from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(
      dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    ARGS:
        - dct: A dictionary-like structure that maps keys to values
        - key: The key can be of any type
        - default: Can either be of type T (generic type) or None.

    Return: Either the value from the dictionary (of any type) or the
    default value of type T.
    """
    if key in dct:
        return dct[key]
    else:
        return default
