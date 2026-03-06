class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count_element = {}
        storage = []

        for num in arr1:
            if num not in count_element.keys():
                count_element[num] = 1
            else:
                count_element[num]  += 1

        for num in arr2:
            if num in count_element:
                storage.extend([num] * count_element[num])
                del count_element[num]

        for num in sorted(count_element.keys()):
            storage.extend([num] * count_element[num])
                    
        return storage