#!/usr/bin/env python3
"""Measure the runtime"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the runtime

    Parameters
    ----------
    n : int
        Number of times to call wait_n
    max_delay : int
        Maximum delay for each call to wait_n

    Returns
    -------
    float
        Average time taken to call wait_n n times
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
