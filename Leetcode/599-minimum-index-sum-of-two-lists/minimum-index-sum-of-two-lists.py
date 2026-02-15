class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dictionary = {}
        min_index = len(list1) + len(list2)
        result = []

        for i in range(len(list1)):
            if list1[i] not in dictionary:
                dictionary[list1[i]] = i

        for i in range(len(list2)):
            if list2[i] in dictionary:
                total =  i + dictionary[list2[i]]
                if total == min_index:
                    result.append(list2[i])
                elif total < min_index:
                    min_index = total
                    result = [list2[i]]
                    
        return result 