class Solution:
    def predictTheWinner(self, nums):
        
        memo = {}
        
        def dp(l, r):
            if (l, r) in memo:
                return memo[(l, r)]
            
            if l == r:
                return nums[l]
            
            pick_left = nums[l] - dp(l + 1, r)
            pick_right = nums[r] - dp(l, r - 1)
            
            memo[(l, r)] = max(pick_left, pick_right)
            return memo[(l, r)]
        
        return dp(0, len(nums) - 1) >= 0