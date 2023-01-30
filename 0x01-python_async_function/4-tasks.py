#!/usr/bin/env python3
"""task_wait_n: takes in 2 int arguments"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> list:
    """task_wait_n: takes in 2 int arguments (in this order): n and max_delay.
    You will spawn wait_random n times with the specified max_delay."""
    tasks = []
    for i in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    return [await task for task in asyncio.as_completed(tasks)]
