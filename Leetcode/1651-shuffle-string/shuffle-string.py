class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        updated_string = [0] * len(s)

        for i in range(len(indices)):
            updated_string[indices[i]] = s[i]
        
        return "".join(updated_string)