class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        currentMax = nums[0]
        currentMin = nums[0]

        answer = nums[0]

        for num in nums[1:]:
            newMax = max(num,num * currentMax, num * currentMin)
            newMin = min(num,num * currentMax, num * currentMin)

            currentMax = newMax
            currentMin = newMin

            answer = max(answer,currentMax)

        return answer