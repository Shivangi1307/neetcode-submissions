class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1

        if n > 0:
            while n:
                res *= x
                n -= 1
        else:
            while n:
                res /= x
                n += 1

        return res