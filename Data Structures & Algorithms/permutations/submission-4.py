class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        combinations = []
        _map = [False for _ in range(len(nums))]
        self.permute_rec(nums, combinations, _map)
        return combinations

    
    def permute_rec(self, nums: List[int],combinations: List[List[int]],_map = [], construction: List[int] = []):
        if len(construction) == len(nums):
            combinations.append([nums[i] for i in construction])          
            

        for i in range(len(nums)):
            if not _map[i]:
                _map[i] = True
                construction.append(i)
                self.permute_rec(nums,combinations,_map, construction)
                construction.pop()
                _map[i] = False
        