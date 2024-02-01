#!/usr/bin/env python3
'''LIFO caching module'''
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''LIFOCache class'''
    def __init__(self):
        '''A constructor'''
        super().__init__()

    def put(self, key, item):
        '''Inserting data into the cache'''
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = list(self.cache_data.keys())[-2]
                del self.cache_data[last_key]
                print(f'DISCARD: {last_key}')

    def get(self, key):
        '''Retriving a value linked with a key'''
        if key is None:
            return None
        for k, v in self.cache_data.items():
            if k == key:
                return self.cache_data.get(k)
        return None
