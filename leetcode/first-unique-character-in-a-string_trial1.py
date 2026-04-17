class Solution:
    def firstUniqChar(self, s: str) -> int:

        store = {}

        for i in range(len(s)):

            if s[i] not in store:
                store[s[i]] = 1
            else:
                store[s[i]] += 1
        
        for i, char in enumerate(s):
            if store[char] == 1:
                return i
            
        return -1