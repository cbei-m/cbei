s = input()
check = [-1 for _ in range(26)]

for p, i in enumerate(s):
    idx = ord(i)-ord('a')
    if check[idx] == -1:
        check[idx] = p
print(*check)