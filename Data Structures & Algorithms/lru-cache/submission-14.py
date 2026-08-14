class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            
            curr = node
            while curr and curr.next:
                prev = curr.prev
                nxt = curr.next
                after = nxt.next

                curr.next = after
                curr.prev = nxt
                nxt.next = curr
                nxt.prev = prev

                if prev:
                    prev.next = nxt
                if after:
                    after.prev = curr
                
            del self.cache[key]

            self.cache[key] = node

            return node.val

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        cacheSize = len(self.cache)
        
        if key in self.cache:
            # find node in cache and update the value
            node = self.cache[key]
            node.val = value
            
            # switch to most recently used
            curr = node
            while curr and curr.next:
                prev = curr.prev
                nxt = curr.next
                after = nxt.next

                curr.next = after
                curr.prev = nxt
                nxt.next = curr
                nxt.prev = prev

                if prev:
                    prev.next = nxt
                if after:
                    after.prev = curr

            del self.cache[key]

            self.cache[key] = node
               
        elif key not in self.cache and cacheSize >= self.capacity:
            lru_key = next(iter(self.cache))
            lru_node = self.cache[lru_key]
            mru_node = self.cache[next(reversed(self.cache))]

            # re-assign pointers
            new_node = ListNode(value, mru_node)
            mru_node.next = new_node

            # add new node to the cache
            self.cache[key] = new_node

            # remove LRU from the cache 
            del self.cache[lru_key]

        else:
            if len(self.cache) == 0:
                new_node = ListNode(value)
                self.cache[key] = new_node
                return 

            # modify DLL pointers for new node at tail
            mru_node = self.cache[next(reversed(self.cache))]
            new_node = ListNode(value, mru_node)
            mru_node.next = new_node

            # add new node to cache
            self.cache[key] = new_node

class ListNode:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.next = next
        self.prev = prev
        