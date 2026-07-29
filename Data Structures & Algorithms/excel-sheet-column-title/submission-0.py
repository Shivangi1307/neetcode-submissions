class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber:
            columnNumber -= 1
            temp = columnNumber % 26
           
            res.append(chr(temp + ord('A')))

            columnNumber //= 26

        return "".join(res[::-1]) 
            