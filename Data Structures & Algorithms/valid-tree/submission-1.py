from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # Tree is a special kind of graph 
        # All nodes must be connected
        # No cycles
        # there must be exactly n-1 edges (more than n-1 creates a loop while less than n-1 creates disconnected nodes)

        if len(edges) != n-1:
            return False

        graph = defaultdict(list)

        for parent,child in edges:
            graph[parent].append(child)
            graph[child].append(parent)

        visited = set()
    
        def dfs(node,parent):

            if node in visited:
                return False


            visited.add(node)

            for neighbour in graph[node]:
                
                if parent == neighbour:
                    continue

                if not dfs(neighbour,node):
                    return False

            return True

       
        if not dfs(0,-1):
            return False

        return len(visited) == n