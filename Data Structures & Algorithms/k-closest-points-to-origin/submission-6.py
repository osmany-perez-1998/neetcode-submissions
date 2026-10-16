
from typing import List,Tuple
import heapq


class KthLargest:

    heap = []
    max_heap : Tuple[int, List[int]]

    def __init__(self, k: int, nums: List[Tuple[int,List[int]]]):
        self.heap = [(-i[0],i[1]) for i in nums[:k]] 
        self.max_heap = min(self.heap)
        
        heapq.heapify(self.heap)

        for i in range(k, len(nums)):
            self.add(nums[i])        


    def add(self, val: Tuple[int, List[int]]):

        if -val[0] < self.heap[0][0]:
            return
        else:
            heapq.heappushpop(self.heap,(-val[0], val[1]))
            self.max_heap = min(self.max_heap,(-val[0],val[1]))

class Solution:
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        _points = [((i[0]**2 + i[1]**2), i) for i in points]
        kth = KthLargest(k,_points)

        return [i[1] for i in kth.heap]