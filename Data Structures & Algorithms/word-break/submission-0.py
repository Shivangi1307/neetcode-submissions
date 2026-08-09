class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(n):

            if not dp[i]:
                continue


            for word in wordDict:

                if s[i:i+len(word)] == word:
                    dp[i + len(word)] = True


        return dp[n]