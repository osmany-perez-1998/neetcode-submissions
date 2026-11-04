class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [0] * (n+1)
        steps[0] = 1
        steps[1] = 1
        for s in range(2, n+1):
            steps[s] = steps[s-1] + steps[s-2]

        print(steps[n])
        return steps[n]