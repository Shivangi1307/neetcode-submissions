class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        total = nums[0]

        currentMax = nums[0]
        maxSum = nums[0]

        currentMin = nums[0]
        minSum = nums[0]

        for num in nums[1:]:
            total += num

            currentMax = max(num, num + currentMax)
            maxSum = max(maxSum,currentMax)

            currentMin = min(num, num + currentMin)
            minSum = min(minSum,currentMin)

        if maxSum < 0:
            return maxSum

        return max(maxSum,total - minSum)
