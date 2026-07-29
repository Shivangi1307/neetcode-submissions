class MyHashSet:

    lst = []
    def __init__(self):
        self.lst = []

    def add(self, key: int) -> None:
        self.lst.append(key)
        return None

    def remove(self, key: int) -> None:
        self.lst = [num for num in self.lst if num != key]
        return None

    def contains(self, key: int) -> bool:
        if key in self.lst:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)