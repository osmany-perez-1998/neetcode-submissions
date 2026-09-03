class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0 for i in range(len(temperatures))]
        s =[0]

        for i in range(1, len(temperatures)):
            while len(s) and temperatures[s[-1]] < temperatures[i]:
                ind = s.pop()
                res[ind] = i - ind

            s.append(i)

        return res
        