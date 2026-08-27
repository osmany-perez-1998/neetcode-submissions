class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        forward = [0 for _ in range(len(nums))]
        backward = [0 for _ in range(len(nums))]

        forward[0]= nums[0]
        backward[-1] = nums[-1]
        for i in range(len(nums)-1):
            forward[i+1] = forward[i]* nums[i+1]
            backward[-2-i] = backward[-1-i]*nums[-2-i]

        result = [0 for i in range(len(nums))]
        result[0]= backward[1]
        result[-1] = forward[-2]
        for i in range(1,len(result)-1):
            result[i] = forward[i-1]* backward[i+1]

        return result
    