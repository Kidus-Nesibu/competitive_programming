for i in range(5):
    col = list(map(int, input().split()))

    if 1 in col:
        row = col.index(1)
        move_count = abs(i - 2) + abs(row - 2)
print(move_count)