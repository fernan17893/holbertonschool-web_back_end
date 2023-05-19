#!/usr/bin/env python3
""" Async task 2 """

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n

async def measure_time(n: int = 0, max_delay:int = 10) -> float:
    """Async routine that measures execution time for wait_n"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()

    total_time = end - start
    return total_time / n
