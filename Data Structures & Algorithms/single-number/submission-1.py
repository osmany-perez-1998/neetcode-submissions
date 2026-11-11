class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        i = 1
        while i < len(nums):
            nums[i] = nums[i]^nums[i-1]
            i+=1
        
        return nums[-1]

    
        