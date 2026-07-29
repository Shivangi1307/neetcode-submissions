class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        found = False
        for a in asteroids:

            while stack and a < 0 and stack[-1] > 0:
                temp = stack.pop()
                if abs(temp) > abs(a):
                    a = temp
                elif abs(temp) == abs(a):
                    found = True
                    break

            if found:
                found = False
                continue
                
            stack.append(a)

        return stack