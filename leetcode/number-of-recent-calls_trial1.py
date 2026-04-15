class RecentCounter:

    def __init__(self):
        self.count = deque()

    def ping(self, t: int) -> int:

        self.count.append(t)

        while self.count and self.count[0] < t - 3000:
            self.count.popleft()

        return len(self.count)