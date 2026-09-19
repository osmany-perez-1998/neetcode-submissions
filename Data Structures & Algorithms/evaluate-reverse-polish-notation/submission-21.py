class Solution:    

    def evaluate(self,operator: str, num1: str, num2: str):
            if operator == "+": return int(num1) + int(num2)
            if operator == "-": return int(num1) - int(num2)
            if operator == "*": return int(num1) * int(num2)
            if operator == "/": return int(num1) / int(num2)
            raise RuntimeError("Invalid operator")
    
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for symbol in tokens:
            try:
                int(symbol)
                stack.append(symbol)
            except ValueError:
                right = stack.pop()
                left= stack.pop()

                stack.append(int(self.evaluate(symbol,left,right)))
        
        return int(stack[-1])


        
        

        