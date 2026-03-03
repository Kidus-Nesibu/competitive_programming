class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
       

        num = 0     
        zero = 0    

        while zero < len(nums) and num < len(nums):
            
            
            if nums[num] != 0:
                num += 1
                continue

            
            if nums[zero] == 0 or zero < num:
                zero += 1
                continue

           
            nums[num], nums[zero] = nums[zero], nums[num]
            num += 1
            zero += 1