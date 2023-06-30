#!/usr/bin/env python3
"""
Redis Module
"""
import redis
from uuid import uuid4
from typing import Callable, Optional, Union
from functools import wraps


UnionOfTypes = Union[bytes, int, float, str]


def count_calls(method: Callable) -> Callable:
    """
    Counts the number
    of calls
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """
        Decoration
        Wrapper
        """
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Stores the history of
    inputs and outputs for
    a particular function
    """
    inputs = method.__qualname__ + ":inputs"
    outputs = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """
        Decoration
        Wrapper
        """
        self._redis.rpush(inputs, str(args))
        returned_method = method(self, *args, **kwds)
        self._redis.rpush(outputs, str(returned_method))
        return returned_method
    return wrapper


def replay(method: Callable):
    """
    Display the history of
    calls of a particular
    function
    """
    self_ = method.__self__
    stored_name = method.__qualname__
    stored_key = self_.get(stored_name)
    if stored_key:
        times = self_.get_str(stored_key)
        inputs = self_._redis.lrange(stored_name + ":inputs", 0, -1)
        outputs = self_._redis.lrange(stored_name + ":outputs", 0, -1)

        print(f"{stored_name} was called {times} times:")
        zipvalues = zip(inputs, outputs)
        result_list = list(zipvalues)
        for k, v in result_list:
            name = self_.get_str(k)
            val = self_.get_str(v)
            print(f"{stored_name}(*{name}) -> {val}")


class Cache:
    """
    Cache Redis Class
    """

    def __init__(self):
        """
        Constructor for
        the Redis Model
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: UnionOfTypes) -> str:
        """
        Stores data into
        the Redis Cache
        """
        key = str(uuid4)
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> UnionOfTypes:
        """
        Gets key from
        Redis
        """
        if fn:
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    def get_str(self, string: bytes) -> str:
        """
        Gets a string
        """
        return string.decode("utf-8")

    def get_int(self, number: int) -> int:
        """
        Gets int value
        """
        result = 0 * 256 + int(number)
        return result