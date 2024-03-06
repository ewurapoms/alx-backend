#!/usr/bin/python3
""" Basecaching Module """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """defines the class"""

    def __init__(self):
        """initializer"""
        super().__init__()
        self.count = {}

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.count[key] += 1
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                low_count = min(self.count.values())
                lower = [
                    k for k, v in self.count.items() if v == low_count
                ]
                lfu_key = min(lower, key=self.count.get)
                self.cache_data.pop(lfu_key)
                self.count.pop(lfu_key)
                print("DISCARD:", lfu_key)

            self.cache_data[key] = item
            self.count[key] = 1

    def get(self, key):
        """Get an item by key"""
        if key is not None and key in self.cache_data.keys():
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.count[key] += 1
            return self.cache_data[key]
        return None
