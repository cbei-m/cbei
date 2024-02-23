l = [0] * 31

for _ in range(28):
    n = int(input())
    l[n] = 1
l[0] = 1
for idx, i in enumerate(l):
    if i==0:
        print(idx)