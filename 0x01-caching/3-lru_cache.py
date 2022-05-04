"""has 1 class inheriting from another file """
from collections import deque


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """class"""

    def __init__(self) -> None:
        """inits """
        super().__init__()
        self.q = deque([])

    def put(self, key, item):
        """assigns an item"""
        if key and item:
            if len(self.q) >= BaseCaching.MAX_ITEMS:
                d = self.q.popleft()
                del self.cache_data[d]
                print("DISCARD: {:s}".format(d))
            if key in self.q:
                self.q.remove(key)
            self.q.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """returns an item"""
        if key and key in self.cache_data.keys():
            self.q.remove(key)
            self.q.append(key)
            return self.cache_data[key]
        return None
