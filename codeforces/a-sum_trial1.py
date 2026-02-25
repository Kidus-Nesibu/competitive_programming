num_input = int(input())

for i in range(num_input):
    nums = [int(num) for num in list(input().split())]
    
    if nums[0] + nums[1] == nums[2]:
        print("YES")
    elif abs(nums[0] - nums[1]) == nums[2]:
        print("YES")
    else:
        print("NO")