price, money, amount = [int(num) for num in input().split()]

total_price = 0
for i in range(1, amount+1):
    total_price += i * price

if money >= total_price:
    print(0)
else:
    print(total_price - money)