w, t = map(int, input().split())

n = int(input())

fallen = False

for _ in range(n):
    wi, ti = map(int, input().split())
    if wi > w or (wi == w and ti < t):  
        fallen = True

if fallen:
    print("The Fallen Champion")
else:
    print("The Champion Saves the Accused")