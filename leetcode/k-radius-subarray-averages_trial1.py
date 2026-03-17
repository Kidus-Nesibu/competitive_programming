class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        result = [-1] * n
        window_sum = 0
        window_size = 2 * k + 1
        
        if n < window_size:
            return result
        
        for i in range(window_size):
            window_sum += nums[i]
        
        result[k] = window_sum // window_size
        
        for i in range(k + 1, n - k):
            window_sum = window_sum - nums[i - k - 1] + nums[i + k]
            result[i] = window_sum // window_size
        
        return result