from typing import List,Tuple
import heapq


class Solution:
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        nums = [(-(i[0]**2 + i[1]**2), i) for i in points]
        
        heap = []
        max_heap = None

        heap = nums[:k] 
        
        heapq.heapify(heap)

        for i in range(k, len(nums)):
            val = nums[i]
            if val[0] >= heap[0][0]:
                heapq.heappushpop(heap,(val[0], val[1]))

        return [i[1] for i in heap]