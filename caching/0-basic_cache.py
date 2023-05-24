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
        """
        checks if both key and item are not None.
        If they are not None,
        it assigns the item value to the key in self.cache_data.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        checks if key is not None. If it is not None,
        it retrieves the value associated with the key from self.cache_data
        using the get method of dictionaries.
        If the key is not found in the dictionary,
        it returns None.
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
