#!/usr/bin/env python3
"""2. Run time for four parallel comprehensions"""

import asyncio
import random
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def measure_runtime() -> float:
    """Measure runtime"""
    start = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = asyncio.get_event_loop().time()
    return end - start
