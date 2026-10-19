from typing import Dict, List

class CountSquares:

    dic_x_y_freq : Dict[int,Dict[int,int]]

    def __init__(self):
        self.dic_x_y_freq = {}
        

    def add(self, point: List[int]) -> None:
        try:
            x = self.dic_x_y_freq[point[0]]
            try:
                x[point[1]] = x[point[1]] + 1
            except KeyError:
                x[point[1]] = 1
        except KeyError:
            self.dic_x_y_freq[point[0]] = {point[1] : 1}
        

    def count(self, point: List[int]) -> int:

        x_coincide = self.dic_x_y_freq.get(point[0], None)        
        
        if not x_coincide:
            return 0
        
        y0 = point[1]
        x0 = point[0]

        count = 0

        for y, freq in x_coincide.items():
            
            dist = abs(y0-y)

            if not dist:
                continue

            factor = freq
            factor1 = freq

            x_right = x0 + dist
            x_left = x0 - dist

            
            try:
                x_right_points = self.dic_x_y_freq[x_right]
                factor *= x_right_points[y]
                factor *= x_right_points[y0]
            except KeyError:
                factor = 0

            try:
                x_left_points = self.dic_x_y_freq[x_left]
                factor1 *= x_left_points[y]
                factor1 *= x_left_points[y0]
            except KeyError:
                factor1 = 0

            count+= (factor + factor1)

        return count




         
        
        