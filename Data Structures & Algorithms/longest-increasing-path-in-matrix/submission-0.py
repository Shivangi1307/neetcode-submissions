class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Memorized DFS  --- DFS + DP

        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0] * cols for _ in range(rows)]

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r,c):

            if dp[r][c] != 0:
                return dp[r][c]

            dp[r][c] = 1
            
            for dr,dc in directions:
                nr = dr + r
                nc = dc + c

                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    dp[r][c] = max(dp[r][c],dfs(nr,nc) + 1)

                
            return dp[r][c] 

        answer = 0
        for r in range(rows):
            for c in range(cols):
                answer = max(answer,dfs(r,c))


        return answer