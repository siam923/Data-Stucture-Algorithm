# Your work here
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.end = None
        self.size = 0


    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.cache:
            return -1
        node = self.cache[key]
        if self.head == node:
            return node.value
        self.remove(node)
        self.set_head(node)
        return node.value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.capacity == 0:
            return 'Cache capacity is 0'
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            if self.head != node:
                self.remove(node)
                self.set_head(node)
        else:
            new_node = Node(key, value)
            if self.size == self.capacity:
                del self.cache[self.end.key]
                self.remove(self.end)
            self.set_head(new_node)
            self.cache[key] = new_node

    def set_head(self, node):
        node.prev = None
        node.next = None
        if self.head == None:
            self.head = node
            self.end = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def remove(self, node):
        if self.head == None:
            return
        if self.head == node and self.end == node:
            self.head = None
            self.end = None
        elif self.end == node:
            node.prev.next = None
            self.end = node.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.size -= 1
        del node


# Test
our_cache = LRU_Cache(5)

print(our_cache.get(7))      # returns -1
print(our_cache.get(9))      # return -1

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))      # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))
 # returns -1 because the cache reached it's capacity and 3 was the least recently used entry


empty_cache = LRU_Cache(0)
print(empty_cache.get(7))      # returns -1

empty_cache.set(3, 3);
print(empty_cache.set(4, 4))  # Cache capacity is 0

print(empty_cache.get(3))      # returns -1
print(empty_cache.get(4))       # returns -1
