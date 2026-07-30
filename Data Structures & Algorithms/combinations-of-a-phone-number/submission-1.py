class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        phone = {
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

            if index == len(digits):
                return ans.append("".join(path))

            
            for ch in phone[digits[index]]:
    
                path.append(ch)

                dfs(index+1)

                path.pop()

        dfs(0)

        return ans