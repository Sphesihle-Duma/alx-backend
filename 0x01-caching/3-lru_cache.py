#!/usr/bin/env python3
'''LRU caching module'''
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    '''LRUCache class'''
    def __init__(self):
        '''A constructor'''
        super().__init__()
        self.access_order = []

    def update_access_order(self, key):
        '''Update the access order when an item is accessed'''
        if key in self.access_order:
            self.access_order.remove(key)
        self.access_order.append(key)

    def put(self, key, item):
        '''Inserting item in a cache'''
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.update_access_order(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = self.access_order.pop(0)
                del self.cache_data[first_key]
                print(f'DISCARD: {first_key}')

    def get(self, key):
        '''Retrieving a value linked with a key'''
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.update_access_order(key)
        return self.cache_data.get(key)
