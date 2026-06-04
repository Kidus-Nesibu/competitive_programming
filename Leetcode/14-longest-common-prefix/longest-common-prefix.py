class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = ""
        strs = sorted(strs)
        first_string = strs[0]
        last_string = strs[-1]

        for i in range(min(len(first_string), len(last_string))):
            if first_string[i] != last_string[i]:
                    return prefix
            else:
                prefix += first_string[i]
        
        return prefix