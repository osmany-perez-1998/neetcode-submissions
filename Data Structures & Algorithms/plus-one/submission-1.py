class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits [-1] = (digits[-1] + 1)%10
        carry = 1 if not digits[-1] else 0

        for i in range(len(digits)-2, -1,-1):
            if not carry:
                break

            digits[i] = (digits[i] + carry) % 10            
            carry = 1 if not digits[i] else 0
        
        return ([1] if carry else []) + digits



        