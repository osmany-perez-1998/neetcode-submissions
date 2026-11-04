import math

class Solution:
    def climbStairs(self, n: int) -> int:
        count_2 = n // 2
        count_1 = n%2

        ans = 0

        for i in range(count_2 + count_1,n+1):
            _min = min(count_2,count_1)
            _max = max(count_2,count_1)
            
            aux = 1
            for j in range(_max+1, i+1):
                aux*=j            

            count_2-=1
            count_1+=2

            ans += int(aux/(math.factorial(_min)))

        return ans