class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        aux = nums[0]

        for i in range(1, len(nums)):
            aux^= nums[i]

        return aux
        