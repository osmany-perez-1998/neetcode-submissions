class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0 for _ in range(n+1)] 
        for i in range(n+1):
            ans[i] = bin(i).count("1")
        return ans