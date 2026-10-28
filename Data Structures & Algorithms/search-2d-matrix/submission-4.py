from typing import List


class Solution:
    def binary_first_bigger_than(self,matrix,target):

        start,end = 0, len(matrix) -1
        ans = -1

        while  start <= end:
            mid = start + (end - start  ) // 2

            if matrix[mid][0] <= target:
                ans = mid
                start = mid+1
            else:
                end = mid - 1
        return ans

    def binary_el_exist(self,nums, target):
        start,end = 0, len(nums) -1

        while  start <= end:
            mid = start + (end - start ) // 2

            if nums[mid] == target:
                return True
            
            if nums[mid] > target:
                end = mid -1
            else:
                start = mid +1
            
        
        
        return False

    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.binary_el_exist(matrix[self.binary_first_bigger_than(matrix,target)],target)