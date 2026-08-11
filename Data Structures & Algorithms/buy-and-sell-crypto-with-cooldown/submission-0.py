class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        free = 0
        hold = float("-inf")
        cooldown = float("-inf")

        for price in prices:

            old_hold = hold
            old_free = free
            old_cooldown = cooldown

            hold = max(old_hold, free - price)
            cooldown = old_hold + price
            free = max(old_free,old_cooldown)

        return max(free,cooldown)