#!/usr/bin/env python3
"""Tasks"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return a asyncio.Task

    Parameters
    ----------
    max_delay : int
        Maximum delay for wait_random

    Returns
    -------
    asyncio.Task
        Task that waits for a random delay"""
    return asyncio.create_task(wait_random(max_delay))
