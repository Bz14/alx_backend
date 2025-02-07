#!/usr/bin/env python3
""" LRU caching """

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU cache class """

    def __init__(self):
        """ constructor """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ put an item to the cache """
        if key is not None and item is not None:
            if key in self.keys:
                self.keys.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.keys.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD: {}".format(lru_key))

            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """ get data from the cache """
        if key is None or key not in self.cache_data:
            return None

        self.keys.remove(key)
        self.keys.append(key)
        return self.cache_data[key]
