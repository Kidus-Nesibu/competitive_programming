class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        result = [[1]]
        
        for i in range(numRows - 1):
            rows = []
            temp = [0] + result[-1] + [0]

            for j in range(len(result[-1]) + 1):
                rows.append(temp[j] + temp[j+1])
            result.append(rows)

        return result

