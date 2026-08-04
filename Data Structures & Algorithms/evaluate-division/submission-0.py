from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)

        for (u,v),val in zip(equations,values):

            graph[u].append((v,val))
            graph[v].append((u,1/val))


        def dfs(curr,target,product,visited):
        
            if curr == target:
                return product

            visited.add(curr)

            for neighbour,weight in graph[curr]:

                if neighbour not in visited:
                    ans = dfs(neighbour,target,product * weight,visited)


                    if ans != -1:
                        return ans

            return -1


        answer = []

        for curr,target in queries:

            if curr not in graph or target not in graph:
                answer.append(-1)
                continue
            
            visited = set()
            product = 1
            answer.append(dfs(curr,target,product,visited))

        return answer