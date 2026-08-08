class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n < 3:
            return 0 if n == 0 else 1
        one,two,three = 0,1,1

        for _ in range(3,n+1):
            one,two,three = two,three,one+two+three


        return three 
