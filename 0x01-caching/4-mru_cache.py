#!/usr/bin/env python3
'''MRU caching module'''
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    '''MRU caching class'''
    def __init__(self):
        '''A constructor'''
        super().__init__()
        self.access_order = []

    def update_access_order(self, key):
        '''Updating access order'''
        if key in self.access_order:
            self.access_order.remove(key)
        self.access_order.append(key)

    def put(self, key, item):
        '''Settings an item to key'''
        if key is not None and item is not None:
            self.update_access_order(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                remove_key = self.access_order.pop(-2)
                del self.cache_data[remove_key]
                print(f'DISCARD {remove_key}')

    def get(self, key):
        '''Retrieving the value linked with the key'''
        if key is None and key is not self.cache_data:
            return None
        self.update_access_order(key)
        return self.cache_data.get(key)
