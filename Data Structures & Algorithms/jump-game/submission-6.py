class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if len(nums) < 2 or nums[0] >= len(nums) -1:
            return True
        
        reach = nums[0]

        for i in range(len(nums)):    
            
            if nums[i] and reach >= i and nums[i] + i > reach:                
                reach = nums[i] + i
            
            if reach >= len(nums) - 1:                
                return True
         

        return False

        
         
        