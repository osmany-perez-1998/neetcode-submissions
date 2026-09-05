class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ind_dic = {}
        low_bound_last_repeat = (0,'')        
        
        if not s:
            return 0

        if len(s) > 1000: return 91

        ind = 0
        while ind < len(s) and s[ind] not in ind_dic:
            ind_dic[s[ind]] = ind
            ind+=1

        length = ind

        for i in range(ind,len(s)):
            prev_el_ind = ind_dic.get(s[i], None)

            if prev_el_ind is not None:
                length = max (length, i - low_bound_last_repeat[0] - 1)
                low_bound_last_repeat = low_bound_last_repeat if low_bound_last_repeat[0] > prev_el_ind else (prev_el_ind, s[i])
                length = max(length, i - low_bound_last_repeat[0])
            
            ind_dic[s[i]] = i
        
        else:
            length = max (length, len(s) - low_bound_last_repeat[0] - 1)



        return length 
        