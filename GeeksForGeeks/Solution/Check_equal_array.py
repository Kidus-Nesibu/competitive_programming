class Solution:
    def checkEqual(self, a, b) -> bool:
        #cod
        a.sort()
        b.sort()
        
        return a == b
