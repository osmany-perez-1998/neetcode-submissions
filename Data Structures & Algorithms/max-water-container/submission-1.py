class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # return 1

        i = 0
        value_i = heights[i]
        j = len(heights) - 1
        value_j = heights [j]
        max_trap = 0


        while i < j:
            max_trap = max(max_trap,min(value_i,value_j)* (j-i))

            if value_i <= value_j:
                i+=1
                value_i = heights[i]
            else:
                j-=1
                value_j = heights[j]

        return max_trap