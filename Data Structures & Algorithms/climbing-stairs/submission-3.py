import math

class Solution:
    def climbStairs(self, n: int) -> int:
        count_2 = n // 2
        count_1 = 0 if count_2 == math.ceil(n/2) else 1
        aux_total = count_2 + count_1

        ans = 0

        for i in range(aux_total,n+1):
            _min = min(count_2,count_1)
            _max = max(count_2,count_1)
            
            aux = 1
            for j in range(_max+1, i+1):
                aux*=j

            aux1 = 1
            for j in range(1, _min+1):
                aux1*= j

            count_2-=1
            count_1+=2

            ans += int(aux/aux1)

        return ans