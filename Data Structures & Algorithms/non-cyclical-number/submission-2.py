class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        while n != 1:
            sum = 0
            while n:
                sum += (n % 10)**2
                n //= 10

            n = sum

            if n in seen:
                return False 
            else:
                seen.add(n)

            
        return True     