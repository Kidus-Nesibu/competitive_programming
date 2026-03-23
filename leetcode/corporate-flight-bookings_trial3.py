class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 1)

        for l, r, seats in bookings:
            diff[l - 1] += seats
            if r < n:
                diff[r] -= seats

        res = [0] * n
        res[0] = diff[0]

        for i in range(1, n):
            res[i] = res[i - 1] + diff[i]

        return res