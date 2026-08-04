from collections import defaultdict,deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if not edges:
            return [0]


        graph = defaultdict(list)
        degree = [0] * n 

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)        

            degree[u] += 1
            degree[v] += 1


        queue = deque()

        for i in range(n):
            if degree[i] == 1:
                queue.append(i)

        remaining = n

        while remaining > 2:
            size = len(queue)
            remaining -= size

            for _ in range(size):
                leaf = queue.popleft()

                for neighbour in graph[leaf]:

                    degree[neighbour] -= 1

                    if degree[neighbour] == 1:
                        queue.append(neighbour)


        return list(queue)