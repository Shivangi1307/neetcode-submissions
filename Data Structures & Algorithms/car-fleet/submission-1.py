class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position,speed))
        cars.sort(reverse = True)
        
        max_time = 0
        fleets = 0
        
        for pos,spd in cars:

            time = (target - pos) / spd

            if time > max_time:
                max_time = time
                fleets += 1

        return fleets  

       