class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        j = i + 1
        #2, 1 ,2 
        for i in range(len(nums)-1):
            j = i + 1
            while j < len(nums)-1 and nums[j] != nums[i]:
                j += 1 

            if abs(j-i) <= k and nums[j] == nums[i]:
                return True   

        return False