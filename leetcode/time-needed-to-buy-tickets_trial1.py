class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque((ticket, idx) for idx, ticket in enumerate(tickets))

        time_taken = 0

        while True:
            ticket_left, idx = queue.popleft()
            ticket_left -= 1
            time_taken += 1

            if ticket_left > 0:
                queue.append((ticket_left, idx))
            elif idx == k:
                return time_taken