class Solution:
    def characterReplacement(self, s: str, k: int) -> int: 

        max_freq_letter= ""
        freq_dic = {}

        max_length = 0
        sliding_window = 0


        for i in range (len(s)):

            if freq_dic.get(s[i],0):
                freq_dic [s[i]] +=1
            else:
                freq_dic[s[i]] = 1

            if sliding_window == 59:
                pass

            

            if not k:
                if i - sliding_window + 1 == freq_dic[s[i]]:
                    max_length = max(max_length,freq_dic[s[i]])
                    
            if freq_dic[s[i]] >= freq_dic.get(max_freq_letter,0):
                max_freq_letter = s[i]

            possible_string_balance = i - sliding_window + 1  - k  - freq_dic[max_freq_letter]
            if possible_string_balance <= 0:
                max_length = max(max_length, i - sliding_window + 1 )
            elif i - sliding_window > max_length:
                freq_dic[s[sliding_window]] -= 1
                sliding_window+=1
                possible_string_balance = i - sliding_window + 1  - k  - freq_dic[max_freq_letter]
                if possible_string_balance <= 0:
                    max_length = max(max_length, i - sliding_window + 1 )
                


            

        return max_length
        