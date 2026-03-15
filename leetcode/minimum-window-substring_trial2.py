class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        missing = len(t)
        l = 0
        start = 0
        min_len = float('inf')

        for r in range(len(s)):
            if s[r] in need:
                if need[s[r]] > 0:
                    missing -= 1
                need[s[r]] -= 1

            while missing == 0:
                if r - l + 1 < min_len:
                    start = l
                    min_len = r - l + 1

                if s[l] in need:
                    need[s[l]] += 1
                    if need[s[l]] > 0:
                        missing += 1
                l += 1

        if min_len == float('inf'):
            return ""
        return s[start:start + min_len]