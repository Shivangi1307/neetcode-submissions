class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []
        path = []

        def dfs(index):

            if index == len(nums):
                return ans.append(path.copy())

            
            path.append(nums[index])
            dfs(index+1)
            path.pop()

            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                index += 1

            dfs(index + 1)

        dfs(0)

        return ans
            