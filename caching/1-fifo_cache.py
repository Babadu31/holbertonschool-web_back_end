#!/usr/bin/python3
"""
Create a class FIFOCache that inherits from BaseCaching and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Create FIFOCache class, perform 'put' and 'get' operations
    and print the current state of the cache after each operation.
    """
    def __init__(self):
        """
        The __init__ method is overloaded to add a new instance variable
        self.queue,
        which will be used to keep track of the insertion order of keys.
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        The put method checks if both key and item are not None.
        If they are not None, it assigns the item value to the key in
        self.cache_data.
        It also appends the key to the self.queue to keep track of the
        insertion order.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.queue.append(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                discarded_key = self.queue.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))

    def get(self, key):
        """
        retrieves the value associated with the key from
        self.cache_data using the get method of dictionaries.
        If the key is not found in the dictionary, it returns None.
        If the number of items in self.cache_data exceeds self.MAX_ITEMS,
        it means the cache is full and
        the FIFO eviction policy needs to be applied.
        The first item inserted into the cache is the first one to be evicted.
        The method pops the first key from self.queue,
        removes the corresponding key-value pair from self.cache_data,
        and prints a "DISCARD" message indicating the discarded key.
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
