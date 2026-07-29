class MyHashMap:

    lst = []
    def __init__(self):
        self.lst = []

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.lst)):
            if self.lst[i][0] == key:
                self.lst[i] = (key, value)
                return None
        self.lst.append((key, value)) 
        return None

    def get(self, key: int) -> int:
        for k, v in self.lst:
            if k == key:
                return v
        return -1
            
    def remove(self, key: int) -> None:
        self.lst = [self.lst[i] for i in range(len(self.lst)) if self.lst[i][0] != key]
        return None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)