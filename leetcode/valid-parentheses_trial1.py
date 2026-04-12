class Solution:
    def isValid(self, s: str) -> bool:

        valid = {
            '(':')',
            '{':'}',
            '[':']'
        }

        stack = []


        for ch in s:

            if ch in  valid.keys():
                stack.append(ch)
            else:
                if not stack:
                    return False
                
                value = stack.pop()
                    
                if valid[value] != ch:
                    return False
        
        return not stack