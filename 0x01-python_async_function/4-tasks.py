#!/usr/bin/env python3
"""
This script simply just alters the code from wait_n
into a new function task_wait_n.
"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    ARGS:
        - n: an integer
        -max_delay: an integer

    RETURN: a list of float values
    """
    # Running task_wait_random concurrently n times
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Gathering the result of the tasks
    batch = await asyncio.gather(*tasks)

    # Sorting the batch in a new list without using sorted()
    sorted_list = []
    for element in batch:
        i = 0
        while i < len(sorted_list) and sorted_list[i] < element:
            i += 1
        sorted_list.insert(i, element)

    return sorted_list
