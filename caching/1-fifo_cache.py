#!/usr/bin/env python3
"""FIFO Cache"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Cache Class"""
    def __init__(self):
        super().__init__()
        self.cache_data = []

    def put (self, key, item):
        """Assigns the value `item` to the key `key` in the dictionary `cache_data`.
      If the key `key` is already in the cache, then the value is overwritten.
      If the cache is full, then the first item in the queue"""
        if key is None or item is None:
            return
        
        self.cache_data.append((key, item))

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(0)
            print("DISCARD: {}".format(key))


    def get(self, key):
        """Returns the value in the dictionary `cache_data`
        linked to the key `key`.If the key `key` is not in the dictionary,
        then `get()` returns `None`."""
        if key is None:
            return None

        if key not in self.cache_data:
            return None

        return self.cache_data.get(key)
