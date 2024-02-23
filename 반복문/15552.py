import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a, b = input().split()
    a, b = int(a), int(b)
    print(a+b)