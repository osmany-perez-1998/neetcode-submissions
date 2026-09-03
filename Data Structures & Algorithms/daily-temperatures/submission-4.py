class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        results = [0 for i in range(len(temperatures))]
        stack =[0]

        for i in range(1, len(temperatures)):
            while len(stack) and temperatures[stack[-1]] < temperatures[i]:
                ind = stack.pop()
                results[ind] = i - ind

            stack.append(i)

        return results
        