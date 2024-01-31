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
            self.cache_data.update(
                {key: item}
                )
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key, value = self.cache_data.popitem()
                print(f'DISCARD: {first_key}')

    def get(self, key):
        '''Retriving a value linked with a key'''
        if key is None:
            return None
        for k, v in self.cache_data.items():
            if k == key:
                return self.cache_data[k]
        return None
