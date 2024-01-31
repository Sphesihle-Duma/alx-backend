#!/usr/bin/env python3
'''
BasicCache
'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Caching class"""
    def __init__(self):
        """ Constructor
        """
        super().__init__()

    def put(self, key, item):
        """ Setting keys in the cache"""
        if key is not None and item is not None:
            self.cache_data.update(
               {key: item}
                )

    def get(self, key):
        '''Returning the value for the key'''
        if key is not None:
            print("test")

    def get(self, key):
        '''returning a value'''
        if key is None:
            return None
        for k in self.cache_data.keys():
            if k == key:
                return self.cache_data.get(key)
        return None
