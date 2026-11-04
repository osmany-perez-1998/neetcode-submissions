import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
                
        _max = max(piles)
        start, end = 0, _max 
        rate = math.ceil( _max / len(piles))

        def valid_rate(rate: int):
            h_needed = 0

            for pile in piles:
                h_needed+= math.ceil(pile / rate)
            
            return h_needed <= h

        while start <= end:
            mid = (start + end) //2

            if mid and valid_rate(mid):
                rate = mid
                end = mid - 1
            else:
                start = mid + 1

        return rate