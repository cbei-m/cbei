h, m = input().split()
h, m = int(h), int(m)

temp = m + (h+24) * 60 - 45

print(temp // 60 % 24, temp%60)