class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n = len(text1)
        m = len(text2)

        dp = [[0] * m for _ in range(n)]
        

        for i in range(n):
            for j in range(m):

                if text1[i] == text2[j]:

                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1

                else:
                    if i == 0:
                        dp[i][j] = dp[i][j-1]

                    elif j == 0:
                        dp[i][j] = dp[i-1][j]

                    else:
                        dp[i][j] = max(dp[i][j-1],dp[i-1][j])

                    

        return dp[n-1][m-1]

                