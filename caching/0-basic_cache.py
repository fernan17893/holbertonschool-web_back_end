#!/usr/bin/env python3
"""BasicCache module"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class"""

    def put(self, key, item):
        """put"""
        if key or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get"""
        if key is None:
            return None

        if key not in self.cache_data:
            return None

        return self.cache_data.get(key)
