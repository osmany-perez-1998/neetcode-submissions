class Solution:    

    
    
    def evalRPN(self, tokens: List[str]) -> int:
        def evaluate(operator: str, num1: str, num2: str):
            if operator == "+": return int(num1) + int(num2)
            if operator == "-": return int(num1) - int(num2)
            if operator == "*": return int(num1) * int(num2)
            if operator == "/": return int(num1) / int(num2)
            raise RuntimeError("Invalid operator")

        stack = []

        for symbol in tokens:
            try:
                int(symbol)
                stack.append(symbol)
            except ValueError:
                right = stack.pop()
                left= stack.pop()

                stack.append(evaluate(symbol,left,right))
        
        return int(stack[-1])


        
        

        