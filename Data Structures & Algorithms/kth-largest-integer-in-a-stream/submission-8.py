from typing import List
import heapq


class KthLargest:

    heap = []
    k : int

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums[:k]   
        self.k = k      
        heapq.heapify(self.heap)

        for i in range(k, len(nums)):
            self.add(nums[i])

        

    def add(self, val: int) -> int:

        print(self.heap)

        if self.heap and val <= self.heap[0]:
            return self.heap[0]
        elif len(self.heap) < self.k:
            heapq.heappush(self.heap,val)
        else:
            heapq.heappushpop(self.heap,val)        

        return self.heap[0]
