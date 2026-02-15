class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = 1
            elif s[i] in s_dict:
                s_dict[s[i]] += 1
        
        for i in range(len(t)):
            if t[i] not in t_dict:
                t_dict[t[i]] = 1
            elif t[i] in t_dict:
                t_dict[t[i]] += 1
        
        if t_dict == s_dict:
            return True
        else:
            return False