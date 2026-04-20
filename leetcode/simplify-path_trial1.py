class Solution:
    def simplifyPath(self, path: str) -> str:
        
        arr = path.split('/')
        stack = []

        for i in range(len(arr)):
            val = arr[i]
            if val == "..":
                if stack:
                    stack.pop()
            elif val == "" or val == ".":
                continue
            else:
                stack.append(val)
        
        return "/" + "/".join(stack)