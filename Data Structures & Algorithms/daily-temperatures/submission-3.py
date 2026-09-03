class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        results = [0 for i in range(len(temperatures))]
        stack =[(temperatures[0], 0)]

        for i in range(1, len(temperatures)):
            while len(stack) and stack[-1][0] < temperatures[i]:
                _, ind = stack.pop()
                results[ind] = i - ind

            stack.append((temperatures[i],i))

        return results
        