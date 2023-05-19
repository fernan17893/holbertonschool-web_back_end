#!/usr/bin/env python3
""" Async task 1 """


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronus coroutine waits for delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int = 0, max_delay: int = 10) -> list:
    """Async routine that spawns wait_random n times"""
    list_delays = []
    for i in range(n):
        delay = await wait_random(max_delay)
        list_delays.append(delay)
    return sorted(list_delays)
