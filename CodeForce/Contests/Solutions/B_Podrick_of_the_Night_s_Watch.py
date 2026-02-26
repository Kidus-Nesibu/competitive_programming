import sys
import math
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
pair_count = defaultdict(int)

for _ in range(n):
    m = int(input())
    seen_today = set()
    
    for _ in range(m):
        s, h = input().split()
        h = int(h)
        seen_today.add((s, h))
    
    for pair in seen_today:
        pair_count[pair] += 1

threshold = math.ceil(0.8 * n)

for count in pair_count.values():
    if count >= threshold:
        print("YES")
        break
else:
    print("NO")