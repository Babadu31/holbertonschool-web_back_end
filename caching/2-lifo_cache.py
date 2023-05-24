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
        self.order = []

    def put(self, key, item):
        """
        assigns the item value to the key in self.cache_data
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.order.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    discard = self.order[-1]
                    del self.cache_data[discard]
                    print("DISCARD: {}".format(discard))
                    self.order.pop(-1)
            self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
        retrieves the value associated with the key from self.cache_data
        using the get method of dictionaries
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
