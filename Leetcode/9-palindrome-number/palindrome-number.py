class Solution:
    def isPalindrome(self, x: int) -> bool:

        num = str(x)
        original = []

        for i in range(len(num)):
            original.append(num[i])
        
        reverse = original[::-1]

        if original == reverse:
            return True
        else:
            return False
        