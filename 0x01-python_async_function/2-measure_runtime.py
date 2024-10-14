#!/usr/bin/env python3
"""
This script creates a function measure_time with integers
n and max_delay as arguments that measures the total execution time
for wait_n(n, max_delay) and returns total_time/n (a float).
"""

import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    This function measures the time taken for the asyncIO
    function wait_n takes to execute.

    ARGS:
        - n: an integer
        - max_delay: an integer for the delay

    RETURN: a floating point number
    """
    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()

    total_time = end_time - start_time

    elapsed_time_interval = total_time / n

    return elapsed_time_interval
