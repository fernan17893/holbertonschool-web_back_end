#!/usr/bin/env python3

import random
import asyncio


async def wait_n(n: int, max_delay: int) -> float:
    """wait_n: takes in 2 int arguments (in this order): n and max_delay.
    You will spawn wait_random n times with the specified max_delay.
    wait_n should return the list of all the delays (float values)."""
    delays = []
    for i in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))
    return [await delay for delay in asyncio.as_completed(delays)]

async def wait_random(max_delay: int = 10) -> float:
    """wait_random: takes in an integer argument (max_delay, with a default value
    of 10) named wait_random that waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay