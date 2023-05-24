#!/usr/bin/env python3
"""
Import async_generator from the previous task and
then write a coroutine called async_comprehension that takes no arguments.
"""


import asyncio
from typing import List


async def async_comprehension() -> List[float]:
    """
    The coroutine will collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers.
    """
    async_generator = __import__('0-async_generator').async_generator
    return [i async for i in async_generator()]
