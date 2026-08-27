class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return -1 if nums[0] != target else 0
        
        l,r = 0, len(nums) - 1
        index = -1
        i = 10
        while l<r and i > 0 :
            aux = int ((l + r) / 2)

            if target in [nums[l], nums[r]]:
                index = l if nums[l] == target else r
                break   
            elif r-l <=1:
                break     
            if nums[aux]< target:
                l = aux
            else:
                r = aux

            print(aux)
            # i-=1
        return index


                

        