class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        from collections import defaultdict

        left = 0
        count = defaultdict(int)
        total_pairs = 0
        result = 0

        for right in range(len(nums)):
            total_pairs += count[nums[right]]
            count[nums[right]] += 1

            while total_pairs >= k:
                result += len(nums) - right
                count[nums[left]] -= 1
                total_pairs -= count[nums[left]]
                left += 1

        return result