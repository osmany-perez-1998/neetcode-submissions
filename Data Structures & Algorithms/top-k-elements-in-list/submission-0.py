class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_freq = 0
        num_freq = {}
        freq_nums = {}
        for num in nums:
            try:
                num_freq[num]+=1
            except KeyError:
                num_freq[num]=1

            if num_freq[num] > max_freq:
                max_freq = num_freq[num]

        aux_list = [{} for i in range(max_freq)]

        for key,value in num_freq.items():
            aux_list[value-1][key] =0

        keys_return=[]
        i =-1
        while len(keys_return) < k:
            keys_return+=list(aux_list[i].keys())
            i-=1
        return keys_return
