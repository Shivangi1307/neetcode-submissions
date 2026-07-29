class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        path = []
        ans = []

        def dfs(index,total):

            if total == target:
                return ans.append(path.copy())

            if index == len(candidates) or total > target:
                return 


            path.append(candidates[index])
            dfs(index+1,total + candidates[index])
            path.pop()

            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1


            dfs(index+1,total)

        dfs(0,0)

        return ans