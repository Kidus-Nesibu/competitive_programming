class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        q = deque(range(1, n+1))
        count = 1

        while len(q) > 1:

            if k == count:
                q.popleft()
                count = 1
            else:
                q.append(q.popleft())
                count += 1
                
        return q[0]