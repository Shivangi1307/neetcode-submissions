class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parent = [i for i in range(len(edges)+1)]

        def find(x):

            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]


        for u,v in edges:
            rootU = find(u)
            rootV = find(v)

            if rootU == rootV:
                return [u,v]
                
            parent[rootU] = rootV


            
        


        

