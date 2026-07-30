class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        ans = []
        path = []

        wordSet = set(wordDict)

        def dfs(start):

            if start == len(s):
                ans.append(" ".join(path))
                return

            for end in range(start,len(s)):

                word = s[start:end+1]

                if word in wordSet:

                    path.append(word)

                    dfs(end + 1)

                    path.pop()

        dfs(0)

        return ans