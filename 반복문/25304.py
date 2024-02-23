money = int(input())

n = int(input())

for _ in range(n):
    a, b = input().split()
    a, b = int(a), int(b)
    money -= a * b

if not money:
    print("Yes")
else:
    print("No")
