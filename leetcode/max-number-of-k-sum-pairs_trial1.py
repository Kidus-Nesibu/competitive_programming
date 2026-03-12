class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        operations = 0
        
        for num in list(counts.keys()):
            target = k - num
            if target in counts:
                if num == target:
                    ops = counts[num] // 2
                else:
                    ops = min(counts[num], counts[target])
                
                operations += ops
                counts[num] -= ops
                counts[target] -= ops
                
        return operations