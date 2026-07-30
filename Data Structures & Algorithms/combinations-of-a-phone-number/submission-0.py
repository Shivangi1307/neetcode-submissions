class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        map = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        if not digits:
            return []

        ans = []
        path = []

        def dfs(index):

            if len(path) == len(digits):
                return ans.append("".join(path))

            
            for i in range(len(map[digits[index]])):
    
                path.append(map[digits[index]][i])

                dfs(index+1)

                path.pop()

        dfs(0)

        return ans