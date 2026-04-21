class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i].isdigit() == False:
                stack.append(s[i])
            else:
                stack.pop()
        value = ''.join(stack)
        print(value)

        return value 