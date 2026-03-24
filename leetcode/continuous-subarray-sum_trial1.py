class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem_index = {0: -1}
        prefix = 0
        
        for i, num in enumerate(nums):
            prefix += num
            
            if k != 0:
                prefix %= k
            
            if prefix in rem_index:
                if i - rem_index[prefix] >= 2:
                    return True
            else:
                rem_index[prefix] = i
        
        return False