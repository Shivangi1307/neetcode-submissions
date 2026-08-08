class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}
        def count(steps):
            
            if steps == n:
                return 1
            
            if steps > n:
                return 0

            if steps in memo:
                return memo[steps]

            memo[steps] = count(steps+1) + count(steps+2)

            return memo[steps]

        return count(0)