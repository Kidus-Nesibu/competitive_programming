class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        left = 0
        right = k - 1

        window_sum = 0
        for i in range(left, right + 1):
            window_sum += nums[i]

        max_sum = window_sum

        while right < len(nums) - 1:

            window_sum -= nums[left]

            left += 1
            right += 1

            window_sum += nums[right]

            if window_sum > max_sum:
                max_sum = window_sum

        return max_sum / k