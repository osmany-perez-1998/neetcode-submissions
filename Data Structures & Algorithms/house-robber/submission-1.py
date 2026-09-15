class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return max(nums)
        
        not_used = nums[-1]
        used = nums[-2]


        for i in range(len(nums)-3, -1, -1):
            aux = used
            used = not_used + nums[i]
            not_used = max(not_used, aux)

        return max(not_used,used)
            
        
        