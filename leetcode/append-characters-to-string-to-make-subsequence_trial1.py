class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        count = 0

        index1 = 0
        index2 = 0
        while index1 < len(s) and index2 < len(t):
            if s[index1] == t[index2]:
                count += 1
                index1 += 1
                index2 += 1
            else:
                index1 += 1
        
        return len(t) - count
        