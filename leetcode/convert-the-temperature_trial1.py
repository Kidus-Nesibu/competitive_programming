class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        
        resultArr = []
        converted = celsius + 273.15
        resultArr.append(round(converted, 5))
        converted = celsius * 1.80 + 32.00
        resultArr.append(round(converted, 5))

        return resultArr
