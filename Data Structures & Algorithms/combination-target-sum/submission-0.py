class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        path = []
        ans = []
        
        def dfs(index,total):

            if total == target:
                return ans.append(path.copy())

            if total > target or index == len(nums):
                return 

            path.append(nums[index])
            dfs(index,total + nums[index])
            path.pop()

            dfs(index+1,total)

        dfs(0,0)

        return ans

            