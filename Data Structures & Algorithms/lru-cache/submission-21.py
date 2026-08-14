class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            mru_node = self.cache[next(reversed(self.cache))]
            curr = self.cache[key]

            if mru_node == curr:
                return curr.val
            
            # remove node from DLL
            prev = curr.prev 
            nxt = curr.next 

            if prev:
                prev.next = nxt
            if nxt:
                nxt.prev = prev
            
            # delete node from position in cache
            del self.cache[key]

            # add updated node to end of DLL 
            mru_node.next = curr
            curr.prev = mru_node

            # update cache
            self.cache[key] = curr

            return curr.val

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        cacheSize = len(self.cache)
        
        if key in self.cache:
            mru_node = self.cache[next(reversed(self.cache))]
            curr = self.cache[key]

            if mru_node == curr:
                curr.val = value
                return
            
            # remove node from DLL
            prev = curr.prev 
            nxt = curr.next 

            if prev:
                prev.next = nxt
            if nxt:
                nxt.prev = prev
            
            # delete node from position in cache
            del self.cache[key]

            # add updated node to end of DLL 
            mru_node.next = curr
            curr.prev = mru_node

            # update cache
            curr.val = value
            self.cache[key] = curr

               
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
        