class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        sign = 1 if x >= 0 else -1
        x_abs = abs(x)
        reversed_x = 0
        
        while x_abs != 0:
            pop = x_abs % 10          # Get last digit
            x_abs //= 10              # Remove last digit
            
            # Check for overflow
            if reversed_x > (INT_MAX - pop) // 10:
                return 0
            
            reversed_x = reversed_x * 10 + pop
        
        return sign * reversed_x