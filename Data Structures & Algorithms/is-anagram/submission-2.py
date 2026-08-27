class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = 0
        balance_dic ={}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in balance_dic:
                if balance_dic[s[i]] == 0:
                    counter+=1
                balance_dic[s[i]]+=1
                if balance_dic[s[i]] ==0:
                    counter-=1
            else:
                balance_dic[s[i]] = 1
                counter +=1
            
            if t[i] in balance_dic:
                if balance_dic[t[i]] == 0:
                    counter+=1
                balance_dic[t[i]]-=1
                if balance_dic[t[i]] ==0:
                    counter-=1
            else:
                balance_dic[t[i]]= -1
                counter+=1

        return counter == 0
        
        