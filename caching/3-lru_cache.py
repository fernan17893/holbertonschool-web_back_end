#!/usr/bin/env python3
"""LRU Caching"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRU Cache Class"""
    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """"""
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if key not in self.keys:
            self.keys.append(key)

        if len(self.keys) > BaseCaching.MAX_ITEMS:
            first = self.keys.pop(0)
            del self.cache_data[first]
            print("DISCARD:", first)

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
