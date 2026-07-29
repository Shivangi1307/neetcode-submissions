class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        path = []

        def dfs(openn,close):

            if openn == n and close == n:
                ans.append("".join(path.copy()))

            
            if openn < n:
                path.append("(")
                dfs(openn+1,close)
                path.pop()

            if close < openn:
                path.append(")")
                dfs(openn,close+1)
                path.pop()

        dfs(0,0)

        return ans

