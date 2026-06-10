class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"
        result = ""

        # Handle negative numbers using 32-bit two's complement
        num &= 0xffffffff

        while num:
            result = hex_chars[num & 15] + result
            num >>= 4

        return result