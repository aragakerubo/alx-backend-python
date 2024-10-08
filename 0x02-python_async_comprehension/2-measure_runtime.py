#!/usr/bin/env python3
"""2. Run time for four parallel comprehensions"""

import asyncio
import time
from typing import List

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Measure runtime"""
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    return end - start
