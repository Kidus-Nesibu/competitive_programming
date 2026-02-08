from collections import Counter

class Solution:
    # Function to check if b is a subset of a
    def isSubset(self, a, b):
        # Count frequency of elements in a
        count_a = Counter(a)
        
        # Check each element in b
        for elem in b:
            if count_a[elem] == 0:  # element missing in a
                return False
            count_a[elem] -= 1     # use up one occurrence
            
        return True
