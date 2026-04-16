class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        friends = [i for i in range(1, n+1)]

        return self.recur(friends, 0, k)

    
    def recur(self, friends, idx, k):

        if len(friends) == 1:
            return friends[0]
        idx = (idx + k - 1) % len(friends)

        friends.pop(idx)
        print(friends,)

        return self.recur(friends, idx, k)

