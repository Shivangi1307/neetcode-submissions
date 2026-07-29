import heapq
import math 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        map = {}
        result = []

        for i in range(0,len(points)):
            dist = math.sqrt(points[i][0]**2 + points[i][1]**2)
            points[i].append(dist)
            
        
        points = [(z,y,x) for x,y,z in points]
        
        heapq.heapify(points)

        print(points)
        while len(result) < k:
            result.append(heapq.heappop(points))

        result = [(z,y) for x,y,z in result]

        return result