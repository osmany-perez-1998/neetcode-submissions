class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        aux = digits[-1] + 1
        digits [-1] = aux%10
        carry = 1 if not digits[-1] else 0
        for i in range(len(digits)-2, -1,-1):
            if not carry:
                break

            aux = digits[i] + carry
            digits[i] = aux % 10            
            carry = 1 if aux == 10 else 0
        
        return ([1] if carry else []) + digits



        