class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        path = []
        ans = []
        used = [False] * len(nums)

        def dfs():

            if len(path) == len(nums):
                return ans.append(path.copy())

            for i in range(len(nums)):

                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i-1] and used[i-1]:
                    continue

                path.append(nums[i])
                used[i] = True

                dfs()

                path.pop()
                used[i] = False

        dfs()

        return ans


        
