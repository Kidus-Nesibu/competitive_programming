class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        result_indices = []
        nums.sort()
        print(nums)

        for i in range(len(nums)):
            if nums[i] == target:
                result_indices.append(i)
        
        return result_indices