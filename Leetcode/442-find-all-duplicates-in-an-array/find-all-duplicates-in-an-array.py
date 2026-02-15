class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        result = []
        nums.sort()

        for i in range(1, len(nums)):
            prev = nums[i - 1]
            if nums[i] == prev:
                result.append(nums[i])
            else:
                continue
        return result