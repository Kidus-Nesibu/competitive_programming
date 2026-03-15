class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        count = {}
        left = 0
        cur_sum = 0
        ans = 0

        for right in range(len(nums)):
            cur_sum += nums[right]
            count[nums[right]] = count.get(nums[right], 0) + 1

            while count[nums[right]] > 1 or right - left + 1 > k:
                count[nums[left]] -= 1
                cur_sum -= nums[left]
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1

            if right - left + 1 == k:
                ans = max(ans, cur_sum)

        return ans