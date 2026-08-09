class Solution:
    def numSquares(self, n: int) -> int:
        
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for i in range(1,n+1):

            square = 1
            while square * square <= i:
                dp[i] = min(dp[i],dp[i - square * square] + 1)

                square += 1

        return dp[n]