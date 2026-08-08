class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        one,two = 0,0
        n = len(cost)

        for i in range(2,n+1):
            curr = min(one + cost[i-2], two + cost[i-1])

            one = two
            two = curr

        return two