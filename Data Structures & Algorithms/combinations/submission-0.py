class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans = []
        path = []

        def dfs(num):

            if len(path) == k:
                return ans.append(path.copy())

            if num > n:
                return 

            path.append(num)
            dfs(num+1)

            path.pop()
            dfs(num+1)

        dfs(1)

        return ans
