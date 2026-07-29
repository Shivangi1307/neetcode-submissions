class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        n = len(prices) - 1
        for i in range(n):
            j =  i + 1

            while j <= n:
                if prices[j] - prices[i] > max:
                    max = prices[j] - prices[i]
                j += 1

        return max