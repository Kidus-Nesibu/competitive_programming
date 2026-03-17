class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)

        for start, end, direction in shifts:
            if direction == 1:
                diff[start] += 1
                diff[end + 1] -= 1
            else:
                diff[start] -= 1
                diff[end + 1] += 1

        result = []
        total_shift = 0
        for i in range(n):
            total_shift += diff[i]
            new_char = chr((ord(s[i]) - ord('a') + total_shift) % 26 + ord('a'))
            result.append(new_char)

        return ''.join(result)