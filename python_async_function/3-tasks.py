#!/usr/bin/env python3
"""
Import wait_random from 0-basic_async_syntax.
Write a function
(do not create an async function, use the regular function syntax to do this)
task_wait_random that takes an integer max_delay and returns a asyncio.Task.
"""


import asyncio
from typing import Callable
from random import uniform


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio Task object that executes the 'wait_random' coroutine.
    """
    wait_random = __import__('0-basic_async_syntax').wait_random
    task = asyncio.create_task(wait_random(max_delay))

    return task
