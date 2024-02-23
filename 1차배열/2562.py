m, idx = 0, 0
for i in range(1, 10):
    t = int(input())
    if m<t:
        m = t
        idx = i
print(m, idx)