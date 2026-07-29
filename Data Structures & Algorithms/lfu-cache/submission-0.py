from collections import defaultdict


class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.freq = 1

        self.next = None
        self.prev = None

class DLL:
    def __init__(self):

        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left

        self.size = 0

    def insert(self,node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        nxt.prev = node

        node.next = nxt
        node.prev = prev

        self.size += 1 

    def remove(self,node):

        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

        self.size -= 1

    def removeLRU(self):
        lru = self.left.next
        self.remove(lru)
        return lru

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.freqmap = defaultdict(DLL)  
        '''
        defultdict(x) if key is missing auto create x() 
        If not present create a  new DDL -> no error
        '''
        self.minFreq = 0  # lowest frequency


    def update(self,node):

        freq = node.freq

        self.freqmap[freq].remove(node)

        if freq == self.minFreq and self.freqmap[freq].size == 0:
            self.minFreq += 1

        node.freq += 1

        self.freqmap[node.freq].insert(node)


    def get(self, key: int) -> int:
        
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.update(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        
        if self.capacity == 0:
            return

        if key in self.cache:

            node = self.cache[key]
            node.val = value

            self.update(node)

            return

        if len(self.cache) == self.capacity:
            lru = self.freqmap[self.minFreq].removeLRU()
            del self.cache[lru.key]

        node = Node(key,value)
        self.cache[key] = node
        self.freqmap[1].insert(node)
        self.minFreq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)