#LRU cache

import collections
# Fixed based on the comment to use OrderedDict
class LRU_Cache:
    def __init__(self, initial_size):
        if initial_size ==0 or initial_size == None:
            raise Exception("Initial Size needs to be >0")
        self.num_entries = initial_size
        self.bucket_cache = collections.OrderedDict()

    #O(n) = Constant
    def get(self, key):
        try:
            value = self.bucket_cache.pop(key)
            self.bucket_cache[key] = value
            return value
        except KeyError:
            return -1
    #O(n) = Constant
    def set(self, key, value):
        try:
            self.bucket_cache.pop(key)
        except KeyError:
            if len(self.bucket_cache) >= self.num_entries:
                # LIFO order if last is true or FIFO order if false.
                self.bucket_cache.popitem(last=False)
        self.bucket_cache[key] = value
# Testing
# TC1
print("Test case 1")
our_cache = LRU_Cache(5)
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);
print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache
our_cache.set(5, 5)
our_cache.set(6, 6)
print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

#TC2 - Size = 1
print("Test case 2")
cache = LRU_Cache(1)
cache.set(1,1)
cache.set(2,2)
print(cache.get(2))

#TC3 - Size = 0
print("Test case 3")
cache = LRU_Cache(0)
cache.set(1,1)
cache.set(2,2)
print(cache.get(2))

#TC4 - Size = Null
print("Test case 4")
cache = LRU_Cache()
cache.set(1,1)
cache.set(2,2)
print(cache.get(2))