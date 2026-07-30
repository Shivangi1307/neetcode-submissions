class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        subsets = [0] * k

        total = sum(nums)

        if total % k != 0:
            return False

        target = total // k

        if max(nums) > target:
            return False

        nums.sort(reverse = True)

        def dfs(index):

            if index == len(nums):
                return True

            for i in range(k):

                if subsets[i] + nums[index] <= target:
                    
                    subsets[i] += nums[index]

                    if dfs(index + 1):
                        return True

                    subsets[i] -= nums[index]

                if subsets[i] == 0:
                    break

            return False

        return dfs(0)