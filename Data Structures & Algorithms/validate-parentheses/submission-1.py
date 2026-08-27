class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        op = ['(','{','[']
        pair_dic={}
        pair_dic[')'], pair_dic['}'], pair_dic[']'] = '(','{','['
        

        for c in s:
            if c in op:
                stack.append(c)
            elif len(stack) and pair_dic[c] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return not len(stack)
        