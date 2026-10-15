import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        neg_stones = [-i for i in stones]
        heapq.heapify(neg_stones)

        while len(neg_stones) > 1:
            stone1 = heapq.heappop(neg_stones)
            stone2 = heapq.heappop(neg_stones)

            dif = stone1 - stone2

            if dif:
                heapq.heappush(neg_stones, dif)
        
        return -neg_stones[0] if neg_stones else 0


        