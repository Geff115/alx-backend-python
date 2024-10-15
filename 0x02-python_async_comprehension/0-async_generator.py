#!/usr/bin/env python3
"""
This script creates a coroutine called async_generator
that takes no argument. The coroutine will loop 10 times,
each time, asynchronously wait 1 second, then yield a
random number between 0 and 10.
"""

import asyncio
import random


async def async_generator() -> float:
    """
    This function has no argument, but rather generates
    a random floating point number between 0 and 10

    yield: a floating point number
    """
    for i in range(10):
        random_number = random.uniform(0, 10)

        await asyncio.sleep(1)
        yield random_number
