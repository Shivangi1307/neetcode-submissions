class Solution:

    def sortColors(self, nums: List[int]) -> None:
        
        count0 = nums.count(0)
        count1 = nums.count(1)
        count2 = nums.count(2)

        nums[:count0] = [0] * count0
        nums[count0:count0+count1] = [1] * count1
        nums[count0+count1:] = [2] * count2