def twoSum(numbers: List[int],l,r, target: int) -> List[tuple]:
    aux =[]
    while l<r:
        current = numbers[l] + numbers[r]
        if current < target:
            l+=1
        elif current > target:
            r-=1
        else:
            aux.append([l,r])
            aux+=twoSum(numbers,l+1,r-1,target)
            
            break
    return aux


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        aux = set()
        for i in range(len(nums)):
            two_sum = twoSum(nums,i+1,len(nums)-1,-nums[i])
            if two_sum:
                for ans in two_sum:
                    aux.add(tuple([nums[i], nums[ans[0]], nums[ans[1]]]))

        return list(aux)