class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join(char.lower() for char in s if char.isalnum())
        for i in range(len(string)//2):
            if string[i]!= string[-i-1]:
                return False

        return True

        