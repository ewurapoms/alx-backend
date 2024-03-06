#!/usr/bin/python3
""" Basecaching Module """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """implements a LIFO caching system"""

    def __init__(self):
        """ initializer"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = list(self.cache_data.keys())[-1]
                self.cache_data.pop(removed)
                print("DISCARD: {}".format(removed))
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key)
