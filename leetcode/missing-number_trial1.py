class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        for i in range(len(nums)):
            result += i - nums[i]
        return result
     #this was the orignial code but find a better way    
    """ for i in range(len(nums)+1):
        if i not in nums:
            return i"""
