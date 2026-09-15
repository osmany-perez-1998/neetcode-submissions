class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums) <= 1:
            return True

        ind = len(nums) - 1

        for i in range(len(nums)-2, -1,-1):
            if nums[i] and ind - i <= nums[i]:
                ind = i
        
        return not ind
                
