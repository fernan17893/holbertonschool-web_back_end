#!/usr/bin/env python3
"""LFU Caching"""


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """LFU Cache Class"""
    def __init__(self):
        super().__init__()
        self.keys = []
        self.count = {}

    def put(self, key, item):
        """Returns the value least frequently used"""
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if key not in self.keys:
            self.keys.append(key)
            self.count[key] = 1
        else:
            self.count[key] += 1

        if len(self.keys) > BaseCaching.MAX_ITEMS:
            min = self.count[self.keys[0]]
            for k in self.keys:
                if self.count[k] < min:
                    min = self.count[k]
            for k in self.keys:
                if self.count[k] == min:
                    del self.cache_data[k]
                    self.keys.remove(k)
                    del self.count[k]
                    print("DISCARD:", k)
                    break

    def get(self, key):
        """Returns the value in the dictionary `cache_data`
        linked to the key `key`.If the key `key`
        is not in the dictionary,
        then `get()` returns `None`."""
        if key is None:
            return None

        if key not in self.cache_data:
            return None

        self.count[key] += 1
        return self.cache_data[key]