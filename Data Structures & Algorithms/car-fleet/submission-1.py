import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        car_speeds = {position[i] : speed[i] for i in range (len(position))}

        position.sort()
        aux_end = 0
        groups = 0
        print(car_speeds)
        print (position)
        for i in range(len(position) -1 , -1, -1):
            time_left = (target- position[i])/car_speeds[position[i]]

            if time_left > aux_end:
                aux_end = time_left
                groups+=1
        
        return groups
        