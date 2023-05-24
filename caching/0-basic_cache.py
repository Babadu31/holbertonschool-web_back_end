#!/usr/bin/python3

"""
Create a class BasicCache that inherits from BaseCaching
and is a caching system
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class perform some put and get operations,
    and print the current state of the cache after each operation.
    """
    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        if key is not None:
            return self.cache_data.get(key)
        return None
