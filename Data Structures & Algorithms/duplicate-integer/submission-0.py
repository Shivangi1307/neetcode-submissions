class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        my_dict = {key: 0 for key in nums}
        for i in range(n):
            if my_dict[nums[i]] == 1:
                return True
            my_dict[nums[i]] = 1
        return False