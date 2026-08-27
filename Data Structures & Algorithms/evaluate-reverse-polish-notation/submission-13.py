class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if len(tokens) == 1: return eval(tokens[0])

        
        ops = ["+", "-", "*", "/"]
        num_stack = tokens[:2]

        i = 2
        while i < len(tokens):
            if tokens[i] in ops:
                snd = num_stack.pop()
                fst = num_stack.pop()
                op = tokens[i]
                num_stack.append(str(int(eval(fst + op + snd))))        
            else: 
                num_stack.append(tokens[i])
            i+=1

        return int(eval(num_stack[0]))
        


        