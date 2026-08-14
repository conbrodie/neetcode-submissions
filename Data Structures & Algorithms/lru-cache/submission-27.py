class Node:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
        
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.add(new_node)

        if len(self.cache) > self.capacity:
            lru_node = self.head.next
            del self.cache[lru_node.key]
            self.remove(lru_node)
        

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.next = self.tail
        node.prev = prev
        self.tail.prev = node

       



        
