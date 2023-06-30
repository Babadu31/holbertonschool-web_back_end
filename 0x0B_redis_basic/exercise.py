#!/usr/bin/env python3
"""holds a cache class"""
import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """counts methods calls"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper function"""
        self._redis.incr(key, 1)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """records call history"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper function"""
        input = str(args)
        self._redis.rpush(key + ':inputs', input)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(key + ':outputs', output)

        return output
    return wrapper


def replay(method: Callable) -> str:
    """display the history of calls of a function"""
    r = redis.Redis()
    key = method.__qualname__
    inputs = r.lrange(key + ':inputs', 0, -1)
    outputs = r.lrange(key + ':outputs', 0, -1)

    print(f'{key} was called {r.get(key).decode()} times:')

    for i, o in zip(inputs, outputs):
        print(f'{key}(*{i.decode()}) -> {o.decode()}')


class Cache():
    """defines a cache"""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """creates a key and stores into redis"""
        key = str(uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Callable = None):
        """gets from redis"""
        if self._redis.exists(key):
            val = self._redis.get(key)
            if (fn):
                val = fn(val)
            return val
        else:
            return

    def get_str(self, key):
        """gets a str from redis"""
        return self.get(key, str)

    def get_int(self, key):
        """gets an int from redis"""
        return self.get(key, int)
