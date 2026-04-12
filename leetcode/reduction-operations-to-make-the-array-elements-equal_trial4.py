class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        unique_nums = sorted(freq.keys(), reverse=True)
        operations = 0
        running = 0

        for num in unique_nums[:-1]:
            running += freq[num]
            operations += running

        return operations