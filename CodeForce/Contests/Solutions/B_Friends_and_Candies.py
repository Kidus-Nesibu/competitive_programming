num_input = int(input())
for i in range(num_input):
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    
    if total % n != 0:
        print(-1)
        continue
    
    target = total // n
    k = sum(1 for x in a if x > target)
    print(k)
