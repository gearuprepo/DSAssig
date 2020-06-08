# LRU Cache
Implementation using OrderedDict to maintain constant order time complexity

* set O(n) = Constant
> * try Popping the key from cache
> * if error, if the size of the cache is full, then pop last time
> * finally, insert into cachea


* get O(n) = Constant
> * Pop from cache to return.
> * insert into cache.

Review Comments Fixed
---------------------
Review 1 - Rewrite code based on OrderedDict
Review 2 - Add boundary test cases

Reference
* Review Comments
* https://docs.python.org/3/library/collections.html#collections.OrderedDict