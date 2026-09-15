class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if len(nums) < 2 or nums[0] >= len(nums) -1:
            return True

        ind = 0
        reach = nums[0]

        i = 0
        while i < len(nums):       
            
            if nums[i] and ind + reach >= i and nums[i] + i > (ind + reach):
                ind = i
                reach = nums[i]
            
            if (ind + reach) >= len(nums) - 1:
                # print(ind+" "+reach)
                return True
            i+=1

        return False

        
         
        