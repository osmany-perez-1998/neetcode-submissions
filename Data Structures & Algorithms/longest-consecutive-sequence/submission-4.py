class Solution:
    def longestConsecutive(self, nums: List[int]):
        if not len(nums):
            return 0

    
        dict_num_to_seq_len = {} # number to sequence length
        max = 0

        for num in nums:
            if dict_num_to_seq_len.get(num):
                continue

            if dict_num_to_seq_len.get(num-1) and dict_num_to_seq_len.get(num+1):
                dict_num_to_seq_len[num] = dict_num_to_seq_len[num-1] + 1 + (dict_num_to_seq_len[num+1])
                dict_num_to_seq_len[num - dict_num_to_seq_len[num-1]] = dict_num_to_seq_len[num]
                dict_num_to_seq_len[num + dict_num_to_seq_len[num+1]] = dict_num_to_seq_len[num]  

            elif dict_num_to_seq_len.get(num-1):
                dict_num_to_seq_len[num] = dict_num_to_seq_len[num-1] + 1
                dict_num_to_seq_len[num - dict_num_to_seq_len[num-1]] = dict_num_to_seq_len[num]

            elif dict_num_to_seq_len.get(num+1):
                dict_num_to_seq_len[num] = dict_num_to_seq_len[num+1] + 1
                dict_num_to_seq_len[num + dict_num_to_seq_len[num+1]] = dict_num_to_seq_len[num]

            else:
                dict_num_to_seq_len[num] = 1

            if dict_num_to_seq_len[num] > max:
                max = dict_num_to_seq_len[num]

        return max


a = Solution()
print(a.longestConsecutive([2,20,4,10,3,4,5]))


            
        
        

        