class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def dfs(index,xor):

            if len(nums) == index:
                return xor

            taken = dfs(index+1,xor^nums[index])

            skip = dfs(index+1,xor)

            return taken + skip

        return dfs(0,0) 