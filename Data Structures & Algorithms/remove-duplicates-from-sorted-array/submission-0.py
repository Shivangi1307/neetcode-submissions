class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    
        i = 0
        j = i+1
        while j < len(nums)-1:
            while j < len(nums)-1 and nums[j] == nums[i]:
                j += 1

            i += 1
            nums[i] = nums[j]

        return  len(set(nums))