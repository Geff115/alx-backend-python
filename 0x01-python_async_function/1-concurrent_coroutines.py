#!/usr/bin/env python3
"""
This script imports wait_random from the previous python
file, creates a async function called wait_n that takes two
int arguments (n and max_delay), spawning wait_random n times
with the specified max_delay. wait_n should return a list of all
the delays (float values).
"""

import asyncio
import random
import importlib
from typing import List


# Dynamically import wait_random from '0-basic_async_syntax'
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    ARGS:
        - n: an integer
        - max_delay: an integer

    RETURN: a floating point number
    """
    # running wait_random concurrently n times
    list_delays = [wait_random(max_delay) for _ in range(n)]

    # Gathering the result of the coroutines
    batch = await asyncio.gather(*list_delays)

    # Sorting the batch in a new list without using sorted()
    # Using insertion sort algorithm
    sorted_list = []
    for element in batch:
        # finding the correct insertion point
        i = 0
        while i < len(sorted_list) and sorted_list[i] < element:
            i += 1
        # inserting the element at the correct position
        sorted_list.insert(i, element)

    # Returning the sorted_list
    return sorted_list
