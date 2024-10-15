#!/usr/bin/env python3
"""
This script creates a coroutine called measure_runtime.
This coroutine will execute another coroutine called
async_comprehension four times in parallel and measures the
total runtime and returns it.
"""

import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    This function takes no argument.

    RETURN: a float
    """
    start_time = time.time()

    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())

    end_time = time.time()

    runtime = end_time - start_time

    return runtime
