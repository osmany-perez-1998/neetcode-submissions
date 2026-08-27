class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams: List[List[int]] =[]
        freq_dic = {}
        for s in strs:
            freq = [0]*26
            for char in s:
                freq[ord(char)-ord('a')]+=1
            aux_freq = map(str, freq)
            anagrams.append(" ".join(aux_freq))
        
        for i in range(len(strs)):
            try:
                freq_dic[anagrams[i]]+=[strs[i]]
            except KeyError:
                freq_dic[anagrams[i]] = [strs[i]]
        
        return list(freq_dic.values())