#!/usr/bin/env python3
"""LIFO Caching"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Cache Class"""
    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Assigns the value `item` to the key `key`
        in the dictionary `cache_data`.If the key `key`
        is already in the cache, then the value is overwritten.
      If the cache is full, then the last item in the queue is discarded.
"""
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if key not in self.keys:
            self.keys.append(key)

        if len(self.keys) > BaseCaching.MAX_ITEMS:
            last = self.keys.pop(-2)
            del self.cache_data[last]
            print("DISCARD:", last)

    def get(self, key):
        """Returns the value in the dictionary `cache_data`
        linked to the key `key`.If the key `key`
        is not in the dictionary,
        then `get()` returns `None`."""
        if key is None:
            return None

        if key not in self.cache_data:
            return None

        return self.cache_data[key]
