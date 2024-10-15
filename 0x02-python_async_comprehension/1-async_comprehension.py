#!/usr/bin/env python3
"""
This script imports a coroutine async_generator
from the previous task, it also takes a coroutine
called async_comprehension that takes no argument.
The coroutine will collect 10 random numbers using an async
comprehension over async_generator, then return the 10 random numbers
"""

import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    This function takes no argument.

    RETURN: a floating point number
    """
    async_list = [i async for i in async_generator()]

    return async_list
