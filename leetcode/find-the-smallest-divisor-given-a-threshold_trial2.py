class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def compute_sum(divisor):
            total = 0
            for num in nums:
                total += (num + divisor - 1) // divisor
            return total
        
        left, right = 1, max(nums)
        answer = right
        
        while left <= right:
            mid = (left + right) // 2
            
            if compute_sum(mid) <= threshold:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return answer