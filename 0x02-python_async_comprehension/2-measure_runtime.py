#!/usr/bin/env python3
""" measure_runtime coroutine that will execute async_comprehension 4 times """

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure_runtime coroutine that will execute
    async_comprehension 4 times """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = time.perf_counter()
    return (end - start)
