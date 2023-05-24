#!/usr/bin/env python3
"""
Module for measuring runtime
"""
import time
import asyncio
from typing import List

def measure_time(n: int, max_delay: int) -> float:
    """
    Returns the time taken for wait_n function
    """
    wait_n = __import__('1-concurrent_coroutines').wait_n

    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()

    return (end - start) / n