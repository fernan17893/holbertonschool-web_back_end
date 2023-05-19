#!/usr/bin/env python3
""" Async task 2 """


from asyncio import run
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Async routine that measures execution time for wait_n"""
    start = time()
    run(wait_n(n, max_delay))
    end = time()
    total_time = end - start
    return total_time / n
