class LinkedListNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LRU_Cache:

    def __init__(self, initial_size=15):
        self.bucket_array = [None for _ in range(initial_size)]
        self.num_entries = 0
        self.master_q = []

    def set(self, key, value):
        # Implement LRU Start, Incase of cache full, delete LRU O(n) = n
        if self.num_entries > len(self.bucket_array) - 1:
            to_be_deleted = self.master_q[0]
            self.delete(to_be_deleted)
        # Implement LRU End

        bucket_index = self.get_bucket_index(key)
        new_node = LinkedListNode(key, value)
        head = self.bucket_array[bucket_index]

        # check if key is already present in the map, and update it's value
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        # key not found in the chain --> create a new entry and place it at the head of the chain
        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node
        self.num_entries += 1

        # Add to master Queue for implementing LRU
        self.master_q.append(key)

    def get(self, key):
        bucket_index = self.get_hash_code(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                # LRU Implementation Start
                temp_q = []
                temp = None
                for ele in self.master_q:
                    if ele == key:
                        temp = ele
                    else:
                        temp_q.append(ele)
                temp_q.append(temp)
                self.master_q = temp_q
                # LRU Implementation End
                return head.value
            head = head.next
        return -1

    def get_bucket_index(self, key):
        bucket_index = self.get_hash_code(key)
        return bucket_index

    def get_hash_code(self, key):
        num_buckets = len(self.bucket_array)
        hash_code = key % num_buckets  # Simple hash code with compression
        return hash_code

    def size(self):
        return self.num_entries

    def delete(self, key):
        bucket_index = self.get_bucket_index(key)
        head = self.bucket_array[bucket_index]

        previous = None
        while head is not None:
            if head.key == key:
                if previous is None:
                    self.bucket_array[bucket_index] = head.next
                else:
                    previous.next = head.next
                self.num_entries -= 1
                return
            else:
                previous = head
                head = head.next

# Testing

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
