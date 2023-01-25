#!/usr/bin/env python3
""" coroutine called async_comprehension that takes no arguments. """

import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """ coroutine called async_comprehension that takes no arguments. """
    result = [i async for i in async_generator()]
    return result
