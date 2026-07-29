from collections import Counter
class CountSquares:

    def __init__(self):
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        
        px,py = point
        ans = 0
        for (x,y), freq in self.points.items():

            if abs(x-px) != abs(y-py) or px == x or py == y:
                continue

            ans += (freq * self.points[(px,y)] * self.points[(x,py)])

        return ans 
