class Solution:    
    def findUnion(self, a, b):
        # code here
        set_a = set(a)
        set_b = set(b)
        
        # Take union of both sets
        union_set = set_a | set_b   # or use set_a.union(set_b)
        
        # Convert to list (driver code can sort it)
        return list(union_set)
