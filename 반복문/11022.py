import sys
input = sys.stdin.readline

n = int(input())

for i in range(1,n+1):
    a, b = input().split()
    a, b = int(a), int(b)
    print(f"Case #{i}: {a} + {b} = {a+b}")