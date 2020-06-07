# LRU Cache
master_q contains the elements in terms of queue that contains the least used elements at the head.

get_hash_code gets the hash code for the given input. Have used a simple integer hashing

* set O(n) = n
> * Incase cache is full, delete from cache using master_q's 0th element
> * check if key is already present in the map, and update it's value
> * key not found in the chain --> create a new entry and place it at the head
> * Add to master Queue for implementing LRU

* get O(n) = 1 (n in case of pulling the LRU)
> *  When accessing an element, push it to the queue end and rearrange.
> * return the actual value