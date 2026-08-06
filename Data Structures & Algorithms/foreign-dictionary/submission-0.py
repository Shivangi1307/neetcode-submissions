from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # same as course schedule 
        # A must come before B ->>> TOPOLOGICAL SORTING


        graph = defaultdict(list)

        for word in words:
            for ch in word:
                graph[ch]


        for i in range(len(words)-1):

            w1 = words[i]
            w2 = words[i+1]

            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            
            for j in range(min(len(w1), len(w2))):

                if w1[j] != w2[j]:
                    graph[w1[j]].append(w2[j])
                    break


        visiting = set()
        visited = set()
        order = []

        def dfs(ch):

            if ch in visiting:
                return False

            if ch in visited:
                return True

            visiting.add(ch)
            for neighbour in graph[ch]:
                if not dfs(neighbour):
                    return False

            visiting.remove(ch)
            visited.add(ch)
            order.append(ch)
            
            return True


        for ch in graph:
            if not dfs(ch):
                return ""

        return "".join(order[::-1])
