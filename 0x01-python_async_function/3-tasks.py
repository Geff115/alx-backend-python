#!/usr/bin/env python3
"""
This script creates a function task_wait_random that
takes an integer max_delay and returns a asyncio.Task.
"""

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    This function returns an asyncio.Task that runs wait_random
    with the specified max_delay.

    ARGS:
        - max_delay: an integer representing the maximum delay.

    RETURN: an asynio.Task that will run wait_random
    """
    task = asyncio.create_task(wait_random(max_delay))

    return task
