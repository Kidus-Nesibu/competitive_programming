class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = []

        for i, (start, end) in enumerate(intervals):
            starts.append((start, i))

        starts.sort()

        res = []

        for start, end in intervals:
            left, right = 0, len(starts) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if starts[mid][0] >= end:
                    ans = starts[mid][1]
                    right = mid - 1
                else:
                    left = mid + 1

            res.append(ans)

        return res