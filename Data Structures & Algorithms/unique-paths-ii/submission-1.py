class Solution:
    def uniquePathsWithObstacles(self, obstracleGrid: List[List[int]]) -> int:
        
        rows = len(obstracleGrid)
        cols = len(obstracleGrid[0])

        dp = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):

                if obstracleGrid[i][j] == 1:
                    continue

                if i == 0 and j == 0:
                    dp[i][j] = 1

                elif i == 0:
                    dp[i][j] = dp[i][j-1]

                elif j == 0:
                    dp[i][j] = dp[i-1][j]

                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[rows-1][cols-1]
