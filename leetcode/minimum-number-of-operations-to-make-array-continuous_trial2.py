class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))

        res = 0
        left = 0

        for right in range(len(nums)):
            while nums[right] - nums[left] >= n:
                left += 1

            res = max(res, right - left + 1)

        return n - res