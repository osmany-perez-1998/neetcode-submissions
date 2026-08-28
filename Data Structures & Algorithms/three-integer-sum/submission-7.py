class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result =set()
        nums.sort()

        for i in range(len(nums)):
            twoSumA = self.twoSum(nums[(i+1):], - nums[i])

            if twoSumA:
                for j in twoSumA:
                    result.add((nums[i], j[0], j[1]))
        
        return [list(el) for el in result]    

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i = 0
        j = len(numbers) -1
        result = []

        while i<j:
            if numbers[i] + numbers[j] == target:
                result.append([numbers[i], numbers[j]])
                i+=1
                j-=1
            elif numbers[i] + numbers[j] < target:
                i+=1
            else:
                j-=1

        return result