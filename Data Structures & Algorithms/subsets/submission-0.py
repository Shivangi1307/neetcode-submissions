class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        path = []
        ans = []

        def dfs(index):

            if index == len(nums):
                return ans.append(path.copy())

            path.append(nums[index])
            dfs(index + 1)

            path.pop()

            dfs(index+1)
            
        dfs(0)

        return ans