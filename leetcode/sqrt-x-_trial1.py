class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        number = 1

        while (number + 1) * (number + 1) <= x:
            number += 1

        return number