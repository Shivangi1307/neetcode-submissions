class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = 0xFFFFFFF
        mask_int = 0x7FFFFFF
        print(mask)
        
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        return a if a <= mask_int  else ~(a ^ mask)