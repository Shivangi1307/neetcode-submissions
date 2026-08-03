from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        dead = set(deadends)

        if "0000" in dead:
            return -1

        queue = deque(["0000"])
        visited = {"0000"}
        

        turns = 0

        while queue:

            for _ in range(len(queue)):

                curr = queue.popleft()

                if curr == target:
                    return turns

                if curr in dead:
                    continue

                for i in range(4):

                    digit = int(curr[i])

                    up = (digit + 1) % 10 
                    nextState = curr[:i] + str(up) + curr[i+1:]

                    if nextState not in dead and nextState not in visited:
                        queue.append(nextState)
                        visited.add(nextState)


                    down = ( digit - 1) % 10
                    nextState = curr[:i] + str(down) + curr[i+1:]

                    if nextState not in dead and nextState not in visited:
                        queue.append(nextState)
                        visited.add(nextState)



            turns += 1

        
        return -1

            