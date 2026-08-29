class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # return 1

        i = 0        
        j = len(heights) - 1
        max_trap = 0


        while i < j:
            max_trap = max(max_trap,min(heights[i],heights[j])* (j-i))

            if heights[i] <= heights[j]:
                i+=1
            else:
                j-=1

        return max_trap