class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        freq_dic = {}

        for i in s1:
            freq_dic[i] = freq_dic.get(i,0) + 1

        matches = 0   
        partial_freq = {}     

        for i in range(len(s2)):            

            if i < len(s1):
                if freq_dic.get(s2[i],0):
                    partial_freq[s2[i]] = partial_freq.get(s2[i], 0) + 1
                    if partial_freq[s2[i]] <= freq_dic[s2[i]]:
                        matches+=1

            else:
                if freq_dic.get(s2[i-len(s1)],0):
                    partial_freq[s2[i-len(s1)]]-=1
                    if partial_freq[s2[i-len(s1)]] >= freq_dic[s2[i-len(s1)]]:
                        pass
                    else:
                        matches -= 1

                if freq_dic.get(s2[i],0):
                    partial_freq[s2[i]] = partial_freq.get(s2[i],0) + 1
                    if partial_freq[s2[i]] > freq_dic[s2[i]]:
                        pass
                    else:
                        matches+=1


            if matches == len(s1):
                return True
        return False