class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        res = 0

        for house in houses:
            left, right = 0, len(heaters) - 1
            first_ge = len(heaters)

            while left <= right:
                mid = (left + right) // 2

                if heaters[mid] >= house:
                    first_ge = mid
                    right = mid - 1
                else:
                    left = mid + 1

            dist_right = heaters[first_ge] - house if first_ge < len(heaters) else float('inf')
            dist_left = house - heaters[first_ge - 1] if first_ge > 0 else float('inf')

            res = max(res, min(dist_left, dist_right))

        return res