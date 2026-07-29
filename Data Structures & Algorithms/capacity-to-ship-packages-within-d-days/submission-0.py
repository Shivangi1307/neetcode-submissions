class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:

            mid = left + (right - left) // 2

            total = 0
            i = 0
            while i < len(weights):
                w_sum = 0
                while i < len(weights) and w_sum + weights[i] <= mid:
                    w_sum += weights[i]
                    i += 1
                total += 1

            if total <= days:
                right = mid 
            else:
                left = mid + 1 

        return left 