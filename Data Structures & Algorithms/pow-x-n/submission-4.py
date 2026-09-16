class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1/ self.myPow(x,-n)

        result = 1
        if n % 2 != 0:
            result*= x
            n-=1
        
        return result * self.myPow(x*x, n//2) 

        