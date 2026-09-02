
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        ordered_tuples = sorted(zip(position, speed))
        time_units = [0.0 for _ in range(len(position))]
        time_units[-1] = (target - ordered_tuples[-1][0]) / ordered_tuples[-1][1]    

        car_fleets = 1
        for i in range(len(ordered_tuples)-2,-1,-1):
            time = (target - ordered_tuples[i][0]) / ordered_tuples[i][1]
            if time <= time_units[i+1]:
                time_units[i] = time_units[i+1]
            else:
                time_units[i] = time
                car_fleets+=1

        return car_fleets