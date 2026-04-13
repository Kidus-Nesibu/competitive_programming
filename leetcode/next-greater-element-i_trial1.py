class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = []
        maximum = 0
        for i in range(len(nums1)):

            for j in range(len(nums2)):

                if nums1[i] == nums2[j]:
                    index = j
                    while index < len(nums2):
                        if nums1[i] < nums2[index]:
                            result.append(nums2[index])
                            break
                        index += 1
                    
                    else: 
                        result.append(-1)
        return result
