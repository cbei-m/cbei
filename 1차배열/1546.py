n = int(input())

l = list(map(int, input().split()))

m = max(l)

print(sum(l)/len(l)/m*100)
