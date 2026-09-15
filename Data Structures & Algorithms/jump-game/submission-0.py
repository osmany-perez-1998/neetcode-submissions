class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums) <= 1:
            return True

        last_true_index = len(nums) - 1

        for i in range(len(nums)-2, -1,-1):
            if nums[i] and last_true_index - i <= nums[i]:
                last_true_index = i
        
        return not last_true_index
                
