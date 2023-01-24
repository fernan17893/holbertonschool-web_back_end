#!/usr/bin/env python3
"""measure_time: takes integers n and max_delay as arguments."""

import time
import asyncio
import random
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """measure_time: takes integers n and max_delay as arguments.
    You will spawn wait_n(n, max_delay) with the specified arguments."""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return (end - start) / n
