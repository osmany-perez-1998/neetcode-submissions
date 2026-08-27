class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        next_high = [0]* len(temperatures)
        num_stack = [(temperatures[0],0)]

        for i in range(1,len(temperatures)):
            if  temperatures[i] > temperatures[i-1]:
                while len(num_stack) and num_stack[-1][0] < temperatures[i]:
                    _,index = num_stack[-1]
                    next_high[index] = i - index
                    num_stack.pop()

            num_stack.append((temperatures[i],i))

        return next_high


        