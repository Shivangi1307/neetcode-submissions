class TrieNode():

    def __init__(self):

        self.children = {}
        self.isEnd = False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        root = TrieNode()
        
        for word in dictionary:

            curr = root

            for ch in word:

                if ch not in curr.children:
                    curr.children[ch] = TrieNode()

                curr = curr.children[ch]

            curr.isEnd = True


        dp = {}

        def dfs(index):

            if index == len(s):
                return 0


            if index in dp:
                return dp[index]

            ans = 1 + dfs(index + 1)

            curr = root

            for j in range(index,len(s)):

                if s[j] not in curr.children:
                    break

                curr = curr.children[s[j]]

                if curr.isEnd:
                    ans = min(ans,dfs(j+1))

            dp[index] = ans
            return ans

        return dfs(0)  
