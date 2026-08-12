class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        total = nums[0]

        currentMax = nums[0]
        maxSum = nums[0]

        currentMin = nums[0]
        minSum = nums[0]

        for i in range(1,len(nums)):
            total += nums[i]

            currentMax = max(nums[i], nums[i] + currentMax)
            maxSum = max(maxSum,currentMax)

            currentMin = min(nums[i], nums[i] + currentMin)
            minSum = min(minSum,currentMin)

        if maxSum < 0:
            return maxSum

        return max(maxSum,total - minSum)
