class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if len(tokens) == 1: return eval(tokens[0])

        
        ops = ["+", "-", "*", "/"]
        num_stack = tokens[:2]

        i = 2
        while len(num_stack) > 1 or i < len(tokens):
            if tokens[i] in ops:
                snd = num_stack.pop()
                fst = num_stack.pop()
                neg = eval(snd+'*'+fst) < 0
                op = tokens[i]
                if tokens[i] == "/":
                    op = "//"
                    fst = str((eval(fst)**2)**0.5)
                    snd = str((eval(snd)**2)**0.5)
                    num_stack.append(str(eval((fst + op + snd) +"*"+ ("-1" if neg else "1"))))
                else:
                    num_stack.append(str(eval(fst + op + snd)))
                       
                print(fst + op + snd)
                print(str(eval(fst + op + snd)))           
            else: 
                num_stack.append(tokens[i])
            i+=1
        return int(eval(num_stack[0]))
        


        