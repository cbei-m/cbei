h, m = input().split()
h, m = int(h), int(m)
gap = int(input())

m = m + gap + h * 60

print(m//60%24, m%60)
