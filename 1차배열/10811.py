n,m = list(map(int, input().split()))

l = [i for i in range(n+1)]

for _ in range(m):
    i, j = list(map(int, input().split()))
    l[i:j+1] = l[j:i-1:-1]
print(*l[1:])
