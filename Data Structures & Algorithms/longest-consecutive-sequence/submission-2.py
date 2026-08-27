class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict: Dict[int, List[bool]]= {}

        if len(nums)== 0:
            return 0
        for num in  nums:
            try:
                dict[num]
                continue
            except KeyError:
                dict[num]=[False,False]
                try:
                    lower =dict[num-1]
                    lower[1]= True
                    dict[num][0]=True
                except KeyError:
                    pass

                try:
                    higher= dict[num+1]
                    higher[0]= True
                    dict[num][1]= True
                except KeyError:
                    pass
        
        max_seq = 1

        while len(dict):
            initial = dict.popitem()
            minimum = initial
            maximum = initial
            seq_len = 1

            while minimum[1][0] or maximum[1][1]:
                if minimum[1][0]:
                    seq_len+=1
                    to_remove = minimum[0]
                    minimum = (to_remove -1 ,dict.pop(to_remove-1))
                    if seq_len > max_seq:
                        max_seq = seq_len
                
                if maximum[1][1]:
                    seq_len+=1
                    to_remove = maximum[0]
                    maximum= (to_remove+1,dict.pop(to_remove+1))
                    if seq_len > max_seq:
                        max_seq = seq_len

        return max_seq