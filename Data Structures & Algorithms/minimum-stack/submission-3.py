class MinStack:

    def __init__(self):
        self.elements = []        
        self.cum_min = []
        

    def push(self, val: int) -> None:
        self.elements.append(val)
        if self.cum_min:
            self.cum_min.append(min(self.cum_min[-1], val))
        else:
            self.cum_min.append(val)

    def pop(self) -> None:
        self.elements.pop()
        self.cum_min.pop()
        

    def top(self) -> int:
        return self.elements[-1] 
        

    def getMin(self) -> int:
        return self.cum_min[-1] 
        
