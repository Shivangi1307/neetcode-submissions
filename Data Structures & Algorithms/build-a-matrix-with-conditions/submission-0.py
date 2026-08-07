from collections import defaultdict,deque
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def topologicalSort(condition):

            graph = defaultdict(list)
            indegree = [0] * (k+1)

            for u,v in condition:
                graph[u].append(v)
                indegree[v] += 1


            queue = deque()

            for node in range(1,k+1):
                if indegree[node]  == 0:
                    queue.append(node)


            order = []

            while queue:

                node = queue.popleft()
                order.append(node)

                for neighbour in graph[node]:

                    indegree[neighbour] -= 1
                    if indegree[neighbour] == 0:
                        queue.append(neighbour)

            if len(order) != k:
                return []

            return order


        rowOrder = topologicalSort(rowConditions)

        if not rowOrder:
            return []

        colOrder = topologicalSort(colConditions)

        if not colOrder:
            return []

        rowPos = {}
        for i,num in enumerate(rowOrder):
            rowPos[num] = i

        colPos = {}
        for i,num in enumerate(colOrder):
            colPos[num] = i 


        matrix = [[0] * k for _ in range(k)]

        for num in range(1,k+1):

            r = rowPos[num]
            c = colPos[num]

            matrix[r][c] = num


        return matrix
        


