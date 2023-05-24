#!/usr/bin/env python3
"""
Import async_comprehension from the previous file and
write a measure_runtime coroutine that will execute
async_comprehension four times in parallel using asyncio.gather.

the four executions are launched in parallel,
they all take place at the same time.
That's why the total time is about 10 seconds,
not 40 seconds.
"""


import asyncio
from typing import List


async def measure_runtime() -> float:
    """
    measure the total runtime and return it.
    """
    async_module = __import__('1-async_comprehension')
    async_comprehension = async_module.async_comprehension

    start_time = asyncio.get_event_loop().time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = asyncio.get_event_loop().time()

    total_runtime = end_time - start_time

    return total_runtime
