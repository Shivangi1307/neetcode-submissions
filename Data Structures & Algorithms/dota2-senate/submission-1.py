from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # GREEDY + QUEUE

        n = len(senate)

        radiant = deque()
        dire = deque()

        for i,senator in enumerate(senate):

            if senator == 'R':
                radiant.append(i)
            else:
                dire.append(i)


        while radiant and dire:

            r = radiant.popleft()
            d = dire.popleft()

            if r < d:
                radiant.append(r+n)

            else:
                dire.append(d+n)

        if radiant:
            return 'Radiant'

        return 'Dire'
