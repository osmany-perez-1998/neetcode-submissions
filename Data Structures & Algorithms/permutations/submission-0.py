class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        combinations = []
        self.permute_rec(nums, combinations)
        return combinations

    
    def permute_rec(self, nums: List[int],combinations: List[List[int]] = [],construction: List[int] = []):
        if len(construction) == len(nums):
            combinations.append([nums[i] for i in construction])
            

        for i in range(len(nums)):
            if i not in construction:
                construction.append(i)
                self.permute_rec(nums,combinations,construction)
                construction.pop()