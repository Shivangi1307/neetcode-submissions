class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
            
        nums = list(set(nums))
        nums.sort()
        lst = [1] * len(nums)
        
        index = 0
        temp = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == temp+1:
                lst[index] += 1
            else:
                index += 1
            
            temp = nums[i]

        lst.sort(reverse = True) 
        return lst[0]
