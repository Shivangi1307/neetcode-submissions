class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        total = sum(matchsticks)

        if total % 4 != 0:
            return False

        target = total // 4

        if max(matchsticks) > target:
            return False

        matchsticks.sort(reverse = True)

        sides = [0,0,0,0]
        def dfs(index):

            if index == len(matchsticks):
                return True

            for i in range(4):

                if sides[i] + matchsticks[index] <= target: 
                    sides[i] += matchsticks[index]


                    if dfs(index + 1):
                        return True

                
                    sides[i] -= matchsticks[index]
                
            return False

        return dfs(0)


