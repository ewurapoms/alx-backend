#!/usr/bin/env python3
""" Module for BaseCaching """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ represents the class attribute"""

    def __init__(self):
        """ defines a basecache initialization """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """ adds to the cache """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ retrieves element by key """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
