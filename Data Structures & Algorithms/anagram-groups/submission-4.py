class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        aux_strs : Dict [str,(str,int)] ={}
        for st in strs:
            try:    
                val = aux_strs[st] 
                aux_strs[st] = (val[0],val[1]+1)
            except KeyError:
                aux_strs[st] = (''.join(sorted(st)),1)

        anagram_subgroups : Dict[str,List[str]]={}

        # print(aux_strs)
        for key, anagram_count in aux_strs.items():
            anagram, count = anagram_count
            try:
                sublist = anagram_subgroups[anagram]
                extension = [key]*count              
                anagram_subgroups[anagram] = sublist+extension
            except KeyError:
                anagram_subgroups[anagram] = [key]*count
            
            

        return list(anagram_subgroups.values())