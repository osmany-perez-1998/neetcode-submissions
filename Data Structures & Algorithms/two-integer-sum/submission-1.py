class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dic:Dict[int,List[int]] ={}
        for i in range(len(nums)):
            try:
                index_dic[nums[i]]
                index_dic[nums[i]]= index_dic[nums[i]]+ [i]
            except KeyError:
                index_dic[nums[i]]= [i]

        for i in range(len(nums)):
            remaining = target - nums[i]
            if index_dic.__contains__(remaining):
                
                if nums[i] == remaining:
                    if len(index_dic[remaining]) >=2:
                        return index_dic[remaining][:2]
                else:
                    return [i, index_dic[remaining][0]]