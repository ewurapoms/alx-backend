#!/usr/bin/python3
""" Baecache Module"""
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """defines base caching"""

    def __init__(self):
        """initializer"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = self.order.pop()
                self.cache_data.pop(removed)
                print("DISCARD: {}".format(removed))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Get an item by key"""
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data.get(key)
