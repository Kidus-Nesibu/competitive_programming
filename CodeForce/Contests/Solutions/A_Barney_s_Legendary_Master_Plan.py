num_input = int(input())
for _ in range(num_input):
    n = int(input())
    a = list(map(int, input().split()))
    moves = 0
    prev = a[0]
    for i in range(1, n):
        if a[i] < prev:
            moves += prev - a[i] 
        else:
            prev = a[i]  
    print(moves)
