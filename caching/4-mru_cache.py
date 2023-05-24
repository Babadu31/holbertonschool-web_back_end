#!/usr/bin/python3
"""
class MRUCache that inherits from BaseCaching and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    class MRUCache that inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """
        initialize the new process
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data
        """
        if key and item:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                discard = self.order.pop()
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Return the value in self.cache_data linked to the key
        """
        if key and key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
