class UnionFind:

    def __init__(self,n):
        self.parent = list(range(n))

    def find(self,x):

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False

        self.parent[pu] = pv
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        edges = [edge + [i] for i,edge in enumerate(edges)]
        edges.sort(key = lambda x : x[2])


        def kruskal(skip = -1, force= -1):

            uf = UnionFind(n)

            edge = 0
            weight = 0

            if force != -1:
                u,v,w,idx = edges[force]

                if uf.union(u,v):
                    edge += 1
                    weight += w

            for i,(u,v,w,idx) in enumerate(edges):

                if skip == i:
                    continue

                if uf.union(u,v):
                    edge += 1
                    weight += w

            
            if edge != n-1:
                return float("inf")

            
            return weight

        minWeight = kruskal()
        critical = []
        pseudoCritical = []

        for i in range(len(edges)):

            if kruskal(skip = i) > minWeight:
                critical.append(edges[i][3])

            elif kruskal(force = i) == minWeight:
                pseudoCritical.append(edges[i][3])


        return [critical,pseudoCritical]