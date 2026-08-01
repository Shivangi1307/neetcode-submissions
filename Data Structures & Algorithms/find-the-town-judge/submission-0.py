from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        inDegree = [0] * (n+1)
        outDegree = [0] * (n+1)

        for a,b in trust:
            outDegree[a] += 1
            inDegree[b] += 1

        for person in range(1,n+1):

            if outDegree[person] == 0 and inDegree[person] == n-1:
                return person

        return -1