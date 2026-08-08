class Solution:

    def robRange(self,nums):
        one,two = 0,0

        for money in nums:
            curr = max(two,one + money)
            
            one = two
            two = curr


        return two

    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        return max(self.robRange(nums[1:]),self.robRange(nums[:-1]))

    