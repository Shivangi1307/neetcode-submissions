class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        path = []

        def dfs():

            if len(path) == len(nums):
                return ans.append(path.copy())

            for i in range(len(nums)):

                if nums[i] in path:
                    continue

                path.append(nums[i])

                dfs()

                path.pop()

        dfs()

        return ans