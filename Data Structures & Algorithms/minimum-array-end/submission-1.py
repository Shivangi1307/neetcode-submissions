class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        ans = x
        bit_pos = 0

        while n:
            if ((x >> bit_pos) & 1) == 0:

                if n & 1:
                    ans |= (1 << bit_pos)

                n >>= 1
            
            bit_pos += 1
            
        return ans
