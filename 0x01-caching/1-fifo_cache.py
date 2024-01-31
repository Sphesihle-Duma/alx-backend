#!/usr/bin/env python3
'''Fifo caching module'''
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''FIFO caching clasee'''
    def __init__(self):
        '''A constructor'''
        super().__init__()

    def put(self, key, item):
        '''Setting a key'''
        if key is not None and item is not None:
            self.cache_data.update(
                {key: item}
                )
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                removed_value = self.cache_data.pop(first_key)
                print(f'DISCARD: {first_key}')

    def get(self, key):
        '''Retrive value linked to a key'''
        if key is None:
            return None
        for k, v in self.cache_data.items():
            if k == key:
                return self_cache.data(k)
        return None
