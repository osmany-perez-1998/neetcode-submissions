class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) <=1:
            return s

        center = [0,0]
        max_palindrome = ""

        i = 0
        while i < len(s) - 1:
            center = [i,i]
            
            while i + 1 < len(s) and s[i+1] == s[i]:
                center[1] +=1
                i+=1
            
            start,end = center[0],center[1]

            for j in range(1,i+1):
                if center[0] - j < 0 or center[1] + j >= len(s):
                    break

                if s[center[0] - j] != s[center[1] + j]:
                    break

                start-=1
                end+=1

            max_palindrome = max_palindrome if len(max_palindrome) > (end-start+1) else s[start:(end+1)]

            i+=1
        return max_palindrome