#!/usr/bin/python3
"""LFU Cache Module"""

from collections import defaultdict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Defines the LFUCache class"""

    def __init__(self):
        """Initializer"""
        super().__init__()
        self.count = defaultdict(int)

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.count[key] += 1
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                lfu_key = min(self.count, key=self.count.get)
                self.cache_data.pop(lfu_key)
                self.count.pop(lfu_key)
                print("DISCARD:", lfu_key)

            self.cache_data[key] = item
            self.count[key] = 1

    def get(self, key):
        """Get an item from the cache"""
        if key in self.cache_data:
            self.count[key] += 1
            return self.cache_data.get(key)
