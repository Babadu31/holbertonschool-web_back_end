#!/usr/bin/python3
"""
class LIFOCache that inherits from BaseCaching and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Create LIFOCache class, perform 'put' and 'get' operations
    and print the current state of the cache after each operation.
    """
    def __init__(self):
        """
        The __init__ method is overloaded to add a new instance variable
        self.stack,
        which will be used to keep track of the insertion order of keys.
        """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        assigns the item value to the key in self.cache_data
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.stack.append(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                discarded_key = self.stack.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))

    def get(self, key):
        """
        retrieves the value associated with the key from self.cache_data
        using the get method of dictionaries
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
