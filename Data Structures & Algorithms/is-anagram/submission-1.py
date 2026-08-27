class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_dic = {}
        if len(s)!= len(t):
            return False
            
        for letter in s:
            if letter in freq_dic:
                freq_dic[letter] +=1
            else:
                freq_dic[letter]=1
        
        for letter in t:
            if letter in freq_dic:
                freq_dic[letter]-=1
                if freq_dic[letter] == 0:
                    freq_dic.pop(letter)
            else:
                return False

        return True


        