#!/usr/bin/env python3
"""BasicCache module"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A simple caching system that inherits from BaseCaching.

  This caching system does not have any limits.

  Attributes:
    cache_data: A dictionary that stores the cached data.

  Methods:
    put(key, item):
      Assigns the value `item` to the key `key` in the dictionary `cache_data`.

    get(key):
      Returns the value in the dictionary `cache_data` linked to the key `key`.
      If the key `key` is not in the dictionary, then `get()` returns `None`.
  """

    def put(self, key, item):
        """Assign to the dictionary self.cache_data the item
            value for the key."""
        if key or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value in the dictionary `cache_data`
        linked to the key `key`.If the key `key` is not in the dictionary,
        then `get()` returns `None`."""
        if key is None:
            return None

        if key not in self.cache_data:
            return None

        return self.cache_data.get(key)
