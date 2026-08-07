class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))

    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return False

        self.parent[px] = py
        return True

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True

        if 1 in nums:
            return False

        uf = UnionFind(len(nums))
        factorOwner = {}
        for i,num in enumerate(nums):
            x = num
            factor = 2
            while factor * factor <= x:

                if x %  factor == 0:

                    if factor in factorOwner:
                        uf.union(i,factorOwner[factor])
                    else:
                        factorOwner[factor] = i 

                    while x %  factor == 0:
                        x //= factor

                factor += 1

            if x > 1:
                if x in factorOwner:
                    uf.union(i,factorOwner[x])
                else:
                    factorOwner[x] = i


        root = uf.find(0)

        for i in range(1,len(nums)):
            if uf.find(i) != root:
                return False


        return True


        